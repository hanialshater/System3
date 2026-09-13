import {mergeComments} from './comments.js';
// A user-supplied fine-grained token lives in memory only. It is sent exclusively to GitHub.
export class GitHub {
  constructor() { this.token = ''; this.repo = 'hanialshater/System3'; }
  async request(path, options = {}) {
    const response = await fetch(`https://api.github.com/repos/${this.repo}/${path}`, {
      ...options, credentials: 'omit', headers: { Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', ...(this.token ? { Authorization: `Bearer ${this.token}` } : {}), ...(options.body ? { 'Content-Type': 'application/json' } : {}) }
    });
    const data = await response.json();
    if (!response.ok) { const e = new Error(response.status === 401 ? 'GitHub rejected the token. Reconnect with a valid token.' : response.status === 403 ? 'GitHub access denied or rate limit reached. Check repository Contents permission.' : data.message || 'GitHub request failed.'); e.status = response.status; throw e; }
    return data;
  }
  async file(path, branch) {
    try {
      const data = await this.request(`contents/${path}?ref=${encodeURIComponent(branch)}`);
      if (!data.content || data.encoding !== 'base64') throw new Error('GitHub did not return the file contents.');
      return { text: new TextDecoder().decode(Uint8Array.from(atob(data.content.replace(/\s/g, '')), c => c.charCodeAt(0))), sha: data.sha };
    } catch (e) { if (e.status === 404) return null; throw e; }
  }
  async load(path, layoutPath, branch) {
    const [source, layout] = await Promise.all([this.file(path, branch), this.file(layoutPath, branch)]);
    if (!source) throw new Error(`Manuscript not found on ${branch}.`);
    return { markdown: source.text, layout: layout ? JSON.parse(layout.text) : null, rawLayout: layout?.text || null };
  }
  async save({ path, layoutPath, markdown, layout, baseMarkdown, baseLayout, readBranch, writeBranch }) {
    if (!this.token) throw new Error('Connect GitHub with a repository token to save.');
    if (!/^[a-zA-Z0-9][a-zA-Z0-9._/-]*$/.test(writeBranch) || writeBranch.includes('..') || writeBranch.endsWith('/')) throw new Error('Choose a valid branch name.');
    // Never permit the editor to write the manuscript directly to main/master.
    if (['main', 'master'].includes(writeBranch)) throw new Error('Save to a review branch, then merge on GitHub.');
    let head; let exists = true;
    try { head = await this.request(`git/ref/heads/${writeBranch}`); }
    catch (e) { if (e.status !== 404) throw e; exists = false; head = await this.request(`git/ref/heads/${readBranch}`); }
    const parent = head.object.sha;
    const current = await this.load(path, layoutPath, parent);
    const base=baseLayout?JSON.parse(baseLayout):null,remote=current.rawLayout?JSON.parse(current.rawLayout):null;
    const design=value=>{if(!value)return null;const copy={...value};delete copy.comments;return JSON.stringify(copy);};
    if (current.markdown !== baseMarkdown || design(remote) !== design(base)) throw new Error('The remote manuscript or layout has changed. Your local draft is safe. Download it, then pull that branch before saving.');
    layout={...layout,comments:mergeComments(base?.comments||[],layout.comments||[],remote?.comments||[])};
    const commit = await this.request(`git/commits/${parent}`);
    const tree = await this.request('git/trees', { method: 'POST', body: JSON.stringify({ base_tree: commit.tree.sha, tree: [
      { path, mode: '100644', type: 'blob', content: markdown },
      { path: layoutPath, mode: '100644', type: 'blob', content: JSON.stringify(layout, null, 2) + '\n' }
    ] }) });
    const next = await this.request('git/commits', { method: 'POST', body: JSON.stringify({ message: 'Update manuscript and page layout from Book Studio', tree: tree.sha, parents: [parent] }) });
    // Non-forced update rejects a concurrent change. Creation fails if another writer won the race.
    await this.request(exists ? `git/refs/heads/${writeBranch}` : 'git/refs', { method: exists ? 'PATCH' : 'POST', body: JSON.stringify(exists ? { sha: next.sha, force: false } : { ref: `refs/heads/${writeBranch}`, sha: next.sha }) });
    return { sha: next.sha, url: `https://github.com/${this.repo}/commit/${next.sha}`,layout };
  }
}

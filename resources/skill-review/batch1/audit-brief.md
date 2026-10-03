You are auditing a Claude skill written by the author of the book System 3 (repo /home/user/System3). This is a READ-ONLY task. Do not modify anything in the repo or in the skill folder.

Do all of the following:
1. Read every file in the skill folder in full: SKILL.md, references/ and scripts/.
2. Run every script on the real book in /home/user/System3/chapters, in every mode its --help offers, under both python3.11 and python3.12. Record crashes, wrong output, false positives and false negatives. Check a sample of hits by hand against the text.
3. Check every concrete claim the skill makes about the repo against the repo as it is now. Paths, file names, protected lines, numbers, "state" snapshots, commands and gate scripts must all exist and be accurate. List what is stale or wrong.
4. Find internal problems: contradictions inside the skill, between this skill and the author's other skills (listed below), and between the skill and the repo's own rules (resources/editorial/easter-egg-register.md and prompts/chapter-version-evaluation.md). Also look for unclear steps, missing steps, instructions a model is likely to misread, and things that make a run slow or wasteful.
5. Judge the description (frontmatter): would it trigger on the right requests and stay quiet on near misses?

The author's other skills, for cross-checking, are in /tmp/claude-0/-home-user-System3/41e64861-d08b-5218-ab73-f3fe01d2b717/scratchpad/author-skills/orig/ (de-llm, dev-edit, fresh-claims, levantine-translate).

Write a prioritised findings list to the file you are given. Each finding must have:
- severity (bug, wrong, stale, gap, polish);
- evidence (file:line, a command and its output, or a quote);
- a concrete proposed fix (exact replacement text or a code change).

Also propose any new script checks that would have caught problems. Keep fixes in the author's style: lean, explained, no shouting.

Reply in under 150 words with the top 5 findings.

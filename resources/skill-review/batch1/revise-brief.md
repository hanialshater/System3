You are revising one of the author's Claude skills (the author wrote the book System 3, repo /home/user/System3 — READ ONLY; never modify it). Work only in the revised skill folder you are given; the original is alongside in ../orig/<skill> for reference.

Inputs to use:
- the audit of this skill (path given) — prioritised findings with proposed fixes;
- findings-from-runs.md in the author-skills folder — what real test runs revealed (only the lines about this skill);
- the test outputs in iteration-1/eval-*/ for this skill (old_skill = original skill, without_skill = no skill), if you want to see behaviour.

How to revise:
1. Fix every bug and wrong/stale item. Re-verify each against the repo before changing it (audits can be wrong). Scripts must run on python3.11 and python3.12; test every mode on the real chapters and on a seeded case that exercises the fix.
2. Fill the gaps that matter most for real use. Prefer one clear explained rule over many MUSTs. Keep the author's voice and structure; this is his skill — improve it, don't rewrite it into a different one. Keep SKILL.md lean (under ~500 lines; push detail to references/).
3. Anything that describes repo "state" goes stale: label it with a date and tell the model to re-derive it from the repo (with the exact command) rather than trust the snapshot.
4. Common rules for all of the author's skills: never invent the author's experiences (mark [AUTHOR: …]); Chapter 13, the divider and 14-scaffolds are protected; seeds and payoffs in resources/editorial/easter-egg-register.md are never explained; lines the author restored or rewrote recently (git log / resources/evaluations/*revert-list*) are not re-cut without saying so; deliver work on copies when the repo is read-only or the user asks for a copy.
5. Description: make it trigger on the right requests and stay quiet on near misses; name the neighbouring skills to use instead.
6. Write CHANGELOG.md at the skill folder root: each change, one line, with the finding it answers. Then run `python3 /root/.claude/skills/synced/337ad68c-6d3b-4fdd-9a9c-4e07306f3099_2f355f1e-e2c4-41ac-bdfe-b533c2042732/skill-creator/scripts/quick_validate.py <skill folder>` (cd to the skill-creator dir and use `python3 -m scripts.quick_validate` if needed) and fix any errors.
Reply in under 200 words: the main changes, what you tested, and anything you chose not to change and why.

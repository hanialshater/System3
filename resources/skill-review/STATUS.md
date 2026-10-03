# Skill review: status — WIP (paused 3 Oct 2026)

Paused at the author's request to save tokens. This file says what's done and how to resume.

## Batch 1: de-llm, dev-edit, fresh-claims, levantine-translate

- **Iteration 1 is done.** The author's skills (old_skill) and no skill (without_skill) were each run on 8 tasks and graded.
  - Pass rate: **93% with the author's skills, 83% without.**
  - Results are in `batch1/results/`, the audits in `batch1/audit-*.md`, and the run findings in `batch1/findings-from-runs.md`.
- **Revised versions** are in `batch1/revised/`. Each has a `CHANGELOG.md`.
  - dev-edit, fresh-claims and levantine-translate are done. They are packaged as `.skill` files in `packaged/`, ready to install.
  - de-llm is **partly revised**. Its reviser was stopped mid-work, so it isn't packaged. Finish it from `audit-de-llm.md` and the grading notes below before using it.
- **Iteration 2 (revised vs original) was not run.** The evals are in `batch1/evals.json`; ids 9–12 are held-out tasks. The automatic checks are in `batch1/grading/auto.py`.
- **Grading notes to apply to de-llm:**
  - Check change-list claims about restored lines mechanically; both runs got this wrong.
  - Dry asides count as jokes.
  - Every kept X/Y needs a reason.

## Batch 2: art-direction, blind-bench, book-build, chapter-to-post

- **Audits done:**
  - art-direction;
  - chapter-to-post;
  - dev-edit: the copy in this batch is identical to batch 1's, so batch 1 covers it.
- **Audits not finished:** blind-bench and book-build. Their audit agents were stopped.
- **Runs:** two chapter-to-post tasks were run with and without the skill. The posts are in `batch2/runs/`. The art-direction runs were stopped.
- **Main findings so far:**
  - **chapter-to-post:**
    - It points to "risk-audit rules" that don't exist.
    - It has no rule against inventing the author's experiences.
    - "About 800 words" is over LinkedIn's 3,000-character limit.
    - It names a de-llm skill that isn't installed.
    - It asks to agree the beats with the author before drafting, which is impossible in a one-shot run.
  - **art-direction:**
    - 25 of 101 anchored images don't resolve in today's PDF, including all of Chapter 9's.
    - The audit script always exits 0.
    - Its column-width rule contradicts the renderer.

## Batch 3: consistency, copyedit, topic-research

Unpacked, with the audit brief written (`batch3/audit-brief.md`). The audits were started, then stopped before finishing.

## Book issues found along the way (not fixed; for the author)

1. Chapter 10 says the scores "ran from 2.26 to 2.636". Chapter 2 says 1.33 → 2.26 in one run, and 2.636 for the best run.
2. Chapter 8, around line 109: "The authors acknowledged…" brings back an attribution that commit ca80ba2 removed as unverified.
3. Chapter 8, line 65: the paper compares *different models*, not "versions".
4. Chapter 8, line 59: "about a quarter of prompts" has no citation.
5. The constitution reference gives 21 January 2026; Anthropic's page says 22 January.
6. Chapter 7, Move 37: "Lee got up and left the room". Accounts differ on whether he was already out. Kellin Pelrine, called "an amateur", co-authored the cited KataGo paper.
7. Chapter 9: "the one player to win a game in that 2016 match" is ambiguous.
8. Chapter 10 says "back channel"; Chapter 8 calls it the "bulletin board".
9. 25 art anchors don't resolve, including all of Chapter 9's (art-direction audit).
10. Structure:
    - the interlude interrupts the Chapter 8 → 9 seam;
    - Chapter 12's closing previews the fable;
    - Part IV is thin: 5,261 words against Part III's 16,408.

## To resume

Scratch workspaces don't survive the session; everything needed is in this folder. To pick up:

1. Finish de-llm.
2. Run iteration 2 for batch 1.
3. Finish the batch 2 and batch 3 audits.
4. Run their evals.
5. Revise and package.

## fable-ending (added 3 Oct, WIP)

Reviewed only. Worth keeping as the single home for the Chapter 13 rules. Fixes noted:
- the risk-audit `decisions.md` it cites isn't in the repo;
- give `resources/editorial/check-eggs.sh` its full path, and name the `BASE` for the git diff check;
- mark the proposed seeds as unconfirmed;
- the other skills should point to it rather than repeat the protection rules.

Suggested tests: a de-LLM pass across Chapters 11–13 (Chapter 13 untouched); "evaluate Chapter 13" (judged as fiction, recorded risks raised once); "tighten my revised fable" (versions with trade-offs).

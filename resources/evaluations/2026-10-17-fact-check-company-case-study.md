# Fact-check: System 3 Company case-study evidence record

checker: fact-checker-system-3 (Beckett) · date: 2026-10-17, checks run about 15:10Z to 15:25Z
record checked: `press/books/system-3/experiments/2026-10-company-case-study/record.md`, with `deploy-marker/` and `plant/` (committed in this repo as `ee44535`, 2026-10-17 15:13Z; working tree clean for that folder)
primary sources: `/home/user/system-3-company` at local HEAD `e84b8784` (still the GitHub default-branch head at 15:15Z), read only; GitHub API GETs (`gh api`); public production site (`curl` GETs); Vercel API (denied, 403)
method: every number in section E recomputed with the stated command (or the nearest exact equivalent); each quote compared with the file it cites; categories compared with `chapters/appendix-note-on-evidence.md` and the VP record's rule (`press/decisions/2026-10-16-vp-books-company-case-study.md`, "Evidence categories": "*run* only where a script reruns it from a committed file"). Nothing in the company repo was edited, committed or fetched (no `git fetch`, no `--unshallow`). The two reruns wrote only to my scratchpad.
status: **review record. Not manuscript text. I propose wordings below; each proposal of mine is marked "needs independent check" and must be checked by someone else.**

## Summary

**Rows: 94.** verified 78 · corrected-with-value 10 · disputed 3 · unverifiable 1 · withdrawn-recommended 2.

**Corrections the writer must use (each "needs independent check", since the corrected value is mine):**

1. **Patterns: 26, not 27.** `ls company/knowledge/patterns` counts `README.md`. 26 pattern files: 22 unstarred, 4 at `*`, 0 at `**` (A9, D, E).
2. **Category team: 14 category managers + 36 sub-area managers + 1 Life Hacks safety reviewer = 51**, not "14 plus 37 strand managers". The list of small teams also leaves out `studio` (2) (A2).
3. **r10 learner walks: 66 files, not 81.** `ls company/reviews/*/*-r10.md` returns 66, and the verdict counts (27 + 20 + 18 + 1) add up to 66. The other 15 of the 81 `*r10*` files are the steward's 2026-10-16 `-r10-reading.md` records (C2).
4. **Ledger: 113.1M tokens over 948 measured runs.** The ledger has 992 rows, and 44 of them have `tokens: null` (E, F).
5. **Local clone: 1,666 commits across all local refs, 367 on the default branch.** `git rev-list --all --count` = 1,666, `git rev-list origin/ccr-4c6c7654-ew9ko1 --count` = 367. The GitHub figure of 2,718 is for the default branch only, so the two numbers measure different things. Writing "1,666 of 2,718" overstates local coverage of the default branch (header, E).
6. **C5's comparison commit:** `59489384f` is the commit the approval *covers* (the builder's addendum commit, "Readiness: … record corrected, W-1137 addendum asks PE-ops to approve", 2026-10-15 23:21Z). It is not the commit that wrote the approval. The test file and the three mutated engine files match it, but two other files the tests load differ between `5948938` and `e84b8784`: `engine-v2.ts` (`d11565bb` vs `5a1b9cd7`) and `studyCatalog.ts` (`43c180a8` vs `0b153be5`). Wording: "a new run at `e84b8784`", not "at the approved state".
7. **C6's retro counts cannot be recomputed from today's files.** `events.jsonl` was backfilled after the retro. In the retro's window (10-14 09:40Z to 10-16 09:50Z) today's file holds **372** dispatch events (all `actor: chief-of-staff`), **5** of them with `batch=`. The retro says 223 and 0. The retro-time version of the file is not in the shallow clone. Cite the retro's numbers as the retro's own measurement at the time; it calls its own matrix "testimony-grade". Do not call them re-checkable. The direction (every logged dispatch by the chief of staff) still holds in today's file.
8. **"Ship it anyway" is an option label the founder picked.** The founder's own recorded word is "Deploy". Both reach the disk second-hand: the record says "recorded by: release-manager (from the words the chief-of-staff relayed from the conversation of 2026-10-17)". Section G should say "chose the option 'Ship it anyway'" (C9, G).
9. **C8's site reading:** the `age` header gives the CDN cache time, not the build time. Fresh values: at 15:16:28Z, `/` returned 200 with `age: 179515`, so it was cached at about **2026-10-15 13:24:33Z**. `/d/heat-the-ammonia-maker` returned 200. `/d/snap-the-magnet`, `/d/where-the-axis-starts`, `/d/raters-reward-agreement` and `/d/left-or-right` returned 404, served as the generic `/404` page (`x-matched-path: /404`, the same response as a nonsense path). The 14:44:59Z deploy run was still `in_progress` at 15:16Z. Write "cached around 13:24Z on 10-15", not "built".
10. **D, "flagged once (operating audit A5)":** A5 says "Yes, plus two more of the same kind". So the audit found it three times, not once.

**Disputed (wording or category; the writer must not use the record's version):**

- **C1, "the company's own COE named a mechanism, not a person" / "Five whys end at the mechanism".** Why 5 ends at a person's act: "The chief of staff took the agent's report as truth and did not check Vercel commit statuses". The fifth action is a checklist line for the chief of staff with no board id, which is prose. Suggested wording (needs independent check): "the COE's four tracked actions target mechanisms; its fifth why and fifth action concern the chief of staff's unchecked trust in a report".
- **C11, category "run" for the company's scratch-repo reproduction.** The VP rule allows "run" only where a script reruns it from a committed file, and the record itself says the reproduction is "not committed, so not rerunnable". It is the COE's account of a reproduction: observed for the COE, testimony for the reproduction.
- **Header line 14, "the founder's own words" among the witnesses outside the model.** Every founder quotation on disk was written down by an agent (chief of staff or release manager), usually from a conversation that is not on disk. The words may be outside the model, but whether they are verbatim is the transcribing agent's testimony. Suggested wording (needs independent check): "the founder's words, as transcribed into the company's records by its agents".
- *Not a dispute, a stale qualifier:* **C1 / C5 "run".** The record says the run becomes reproducible "once the head of book commits the folder". The folder was committed as `ee44535` (15:13Z), and both my reruns reproduce the results. "Run" now holds for the C1 trigger logic and for C5's 15 rows at `e84b8784`. The record's text needs updating, not downgrading. Listed here so the writer does not copy the conditional.

**Unverifiable now:** whether production was deployed by a path that leaves no GitHub commit status (Vercel CLI, dashboard). `GET /v7/deployments` for the project returned 403 ("Not authorized: … scope hanis-projects-2e2b67f6"). Only the founder or someone with Vercel access can close this.

**Withdrawn-recommended (I agree with the record):** "one in six reviewers corrected the brief" (C2) and "the backend engineer caught the Neon step" (C3). No source on disk supports either.

**Reruns.** `deploy-marker/replay.sh` with `TMPDIR` set to my scratchpad gives output identical to `replay-result-2026-10-17.txt`. The six saved messages and `vercel.json.at-aefb10a` match the GitHub API byte for byte. `plant/plant.mjs` on a fresh `git archive` of `e84b8784` in my scratchpad gives "15 of 15 applied mutations caught; baseline 42/42; after restore 42/42", with every failing count equal to the readiness record's. The company checkout's `git status` was clean afterwards.

## Claim table

Abbreviations: CR = company repo `/home/user/system-3-company`; API = GitHub REST API.

### Header and section A

| # | Claim | Record location | Source checked | Status | Note |
|---|---|---|---|---|---|
| 1 | Local HEAD `e84b8784`, 2026-10-17 14:21:02Z; default branch `ccr-4c6c7654-ew9ko1` | line 10 | `git log -1`; API repo `default_branch` | verified | Still the API head at 15:15Z. |
| 2 | Clone shallow, 6 boundary commits | line 11 | `git rev-parse --is-shallow-repository`; `wc -l .git/shallow` | verified | true; 6. |
| 3 | "Local git log sees 1,666 commits; the GitHub API sees 2,718 on the default branch" | line 11; E | `git rev-list --all --count`; `git rev-list origin/ccr-4c6c7654-ew9ko1 --count`; API Link `rel="last"` | corrected-with-value | 1,666 is across all local refs; the local default branch has **367**. 2,718 verified. See correction 5. |
| 4 | 48 roles `sonnet`, 49 `inherit`, 2 unset; trailers name Claude Opus | line 14; E | node over `roles.mjs`; commit trailers | verified | The 2 unset are `founder` and `illustrator`. Trailers: "Claude Opus 5.5". |
| 5 | Lessons described as "60-second interactive lessons, one idea per card in a vertical feed"; "a learner predicts, plays and then sees why" | A1 | CR `company/README.md` 3-4 | verified | Verbatim (the source bolds part of it). |
| 6 | Mission line "Leave people better able to ask the next question than we found them" | A1 | `company/mission.md` 3 | verified | Verbatim. |
| 7 | Mission refusals and the EXP-002 line | A1 | `mission.md` 7-8, 22-36 | verified | The refusals run to line 31. |
| 8 | Surface Value v1 order; engagement "never used to rank lessons"; owner founder, protected | A1 | `company/product/surface-value.md` 1-20 | verified | Verbatim (the source bolds "never"). |
| 9 | "System 3 Company exists to test the book's ideas" | A1 | `2026-10-15-founder-press-sibling-company.md` line 11 | verified | Verbatim. |
| 10 | 99 roles; 98 agent files; every role but the founder is a subagent | A2; E | node one-liner; `ls .claude/agents \| wc -l`; set comparison | verified | The only role with no agent file is `founder`. |
| 11 | Teams: categories 51 = 14 CMs + 37 strand managers; leadership 8, design 6, quality 6, platform 3, product 3, research 3, international 3; 1-2 each for backend, growth, company-tools, insight, personalization, rnd, courses, marketing | A2 | node, grouped by `team` and `title` | corrected-with-value | 14 CMs + **36** sub-area managers + 1 `lifehacks-safety-reviewer`. `studio` (2) is missing from the list. Other counts verified. |
| 12 | Founder reports to nobody; 8 named roles report directly to the founder | A2 | `reportsTo` in `roles.mjs` | verified | `reportsTo: "nobody"`; the same 8 ids. |
| 13 | Org-chart quote "Builders cannot promote their own work, and the people who judge it do not work for the people who want it shipped"; five quality roles report to the evaluation steward | A2 | `company/org-chart.md` 31-32; `roles.mjs` | verified | Verbatim. Note: `lifehacks-safety-reviewer` also reports to the steward (6 in all), and the `quality` team of 6 includes the steward. |
| 14 | "26 roles/25 agents" at founding (progress.md 2341); "72 roles in total" (2282); README still says "26 narrow roles" | A2 | `progress.md` 2341, 2282; `README.md` 64 | verified | All verbatim. |
| 15 | Founder mission quote from `roles.mjs` line 26; org chart "desire layer · Surface Value · constitution" | A2 | `roles.mjs` 26; `org-chart.md` 5 | verified | Verbatim. |
| 16 | Org-and-dispatch rule: CoS may not create roles…; "the founder approves every one"; dispatch "only after asking the owning manager" | A2 | `2026-10-16-founder-org-and-dispatch-rule.md` rules 1-3 | verified | Verbatim (the source bolds the phrases). |
| 17 | Persona names Ada, Leonie, Hilde in `people.mjs` | A2 | `tools/org/people.mjs` 8, 9, 30 | verified | |
| 18 | System 3 Meta "parked until First Light ends" | A2 | `2026-10-16-founder-system3-meta-sibling.md` line 8 | verified | |
| 19 | Operating loop "state of the company → choose a move → dispatch the narrowest role → observe → update the state"; "Deep Mode for the company" | A3 | `operating-loop.md` 5-9; `roles.mjs` 55; `org-chart.md` 9 | verified | Verbatim. |
| 20 | `CLAUDE.md` line 5 quote "The disk is the memory: …" | A3 | CR `CLAUDE.md` 5-6 | verified | Verbatim. The sentence runs onto line 6. |
| 21 | progress.md is "testimony from a worker who no longer exists: check what you rely on"; 269 entries | A3; E | `progress.md` 3-4; `grep -c '^## '` | verified | 269. |
| 22 | F-39 personal memory (learner-evaluator item 7); 298 memory files | A3; E | `company/roles/learner-evaluator.md` 70; `find … \| wc -l` | verified | 298. |
| 23 | `dispatch-check.mjs` exits 1 to refuse a dispatch | A3 | `operating-loop.md` 17-19 | verified | The exit-1 sentence is at line 19, just outside the cited 14-18. |
| 24 | `launchGates()` conditions incl. "verified by its own builder" (146), `**` needs human-learner evidence (153-154) | A4 | `tools/company.mjs` 139-157 | verified | Line numbers exact. |
| 25 | `company publish` runs the gates, then writes `published`; no dry-run flag | A4; C14 | `company.mjs` 521-540; `grep dry` | verified | No "dry" anywhere in `company.mjs`. |
| 26 | `CLAUDE.md` line 18 quote (claims, "Builders never mark their own claims verified") | A4 | `CLAUDE.md` 18 | verified | Verbatim. |
| 27 | Claim schema by example; c5 note "before that disputed by fact-checker 2026-10-17 (rule sentence reversed)"; c3 note "a fresh instance that did not write this claim" | A4; C14 | `src/demos/math/left-or-right/meta.json` | verified | Both verbatim. The c5 history also says the rewrite was "from the fact-check's suggestion". |
| 28 | Independence rules protected; rules 1, 6, 7 at the stated lines and wording | A5 | `company/reviews/README.md` 3, 19-22, 31-34 | verified | Verbatim. |
| 29 | Rendered example begins with the simulated-learner line and has both headings | A5 | `company/reviews/adding-squashes-the-photo/2026-10-14-learner-adult-beginner-r10.md` | verified | Lines 1, 9, 24. |
| 30 | `CLAUDE.md` line 20 "Objections travel with decisions. Never answer one with 'noted'." | A6 | `CLAUDE.md` 20 | verified | The source has double quotes around "noted"; that is a punctuation convention. |
| 31 | `check` fails a decision without `owner:` or `## Objections` | A6 | `decisions/README.md` 21-22; `company.mjs` 289-290 | verified | |
| 32 | Constitution Article 4.2 quote; purpose line "may not let the thing being judged quietly change what judges it"; Article 4.1 override | A6; A7 | `constitution.md` 3-4, 50-53 | verified | Verbatim. |
| 33 | Protected paths (lines 3-11); hook "best effort for Bash", "CI is the backstop" | A7 | `protected-paths.txt`; `.claude/hooks/protect-constitution.mjs` 4-5 | verified | |
| 34 | "The judged do not amend the judge alone" (40-41); board membership (37-39) | A7 | `constitution.md` | verified | Verbatim. |
| 35 | Amendment register (AMD-000 "approved by its author", 002, 012 ratified; 001 in part; 005/006/008/010/011 proposed; 003/004/007/009 reserved) | A7; E | `amendments/README.md`; status lines; `AMD-000` 19-21 | verified | Citation fix: the README table (lines 7-16) has no rows for AMD-003, AMD-004 or AMD-012. The 003/004 reservation is sourced at `AMD-005-operating-gates.md` line 6 ("AMD-003 and AMD-004 are reserved by the 2026-10-14 constitutional review"). AMD-012's status comes from its own file, line 3. |
| 36 | Deploy rule decided 2026-10-14 because WIP pushes used the 100 free deployments a day | A8 | `2026-10-14-deploy-needs-founder-approval.md` | verified | |
| 37 | Release log owner and scheme; nine entries r1-r9 | A8; E | `releases.json` | verified | owner release-manager; scheme "rN (sequential…)". |
| 38 | F-48: `git.deploymentEnabled: false`; only the workflow deploys; `CLAUDE.md` 21 stale | A8 | F-48 record lines 13-16; `vercel.json` 8; `CLAUDE.md` 21 | verified | The `CLAUDE.md` text is still stale at HEAD. |
| 39 | 16 rituals with "Remove it if…"; 68 records incl. 7 COEs, 8 WBRs, 11 retros | A9; E | `rituals/README.md` rows 14-29; `ls records` grouped | verified | |
| 40 | 27 patterns; 23 unstarred, 4 `*`, none `**`; quote "was '**' … EXP-001, the test of it, is 'designed, not run'" | A9; D; E | `ls`, `grep -h '^confidence'` | corrected-with-value | **26** patterns: 22 unstarred, 4 `*`, 0 `**`. The quote is verbatim with a fair ellipsis (`artifact-before-account.md` line 3). |
| 41 | EXP-001 and EXP-002 "designed, not run"; EXP-004-008 registered or committed, none run; 8 numbered, 0 with a result | A9; E | status lines; `## Result` sections | verified | EXP-003 has only "Interim data (not a result yet)". There is also an unnumbered prediction file, `2026-10-16-lifehacks-launch-prediction.md`, with no result. |

### Section B (timeline)

| # | Claim | Record location | Source checked | Status | Note |
|---|---|---|---|---|---|
| 42 | Repo created 22:35; first commit `40999183` 22:51 (no parent); `7629eeb9` 23:03 | B | API `created_at` 22:35:38Z; API page 2718; `git log` | verified | |
| 43 | Founding session numbers and quote "That means they work, not that they teach" | B | `progress.md` 2339-2344; `b7fb8bc8` | verified | |
| 44 | 10-13: 178 → 248 → 328 → 504; "53 of 72 roles have never been dispatched"; usage-limit COE ~02:40, 8 of 9 builders | B | `progress.md` 2279-2338; `2026-10-13-coe.md` 1, 6 | verified | Testimony, as the record labels it. |
| 45 | 10-14: `f868127` 12:58; AMD-002 ratified 13:09; three SEV2s 15:27; `dispatch-check` 18:25; PR #2 merged as drafts | B | the three 10-14 COEs; `coe-ci-queue.md` 13; `prs/2.md` 7 | verified | |
| 46 | r6 `41ecec1` 01:07, Vercel "Deployment has completed" 01:12 | B | API statuses (fresh) | verified | 01:12:04Z. |
| 47 | 10-16 19:11 r8 "Deployment rate limited"; `cdee168c` 20:28 | B | API statuses; `git log -1 cdee168c` | verified | 19:11:29Z; 20:28:32Z. |
| 48 | 10-17 deploy runs 08:19, 08:25, 08:32, 10:10, 12:29 failure; one in progress at 14:44 | B; C8 | API `actions/workflows/deploy.yml/runs`, `/jobs` | verified | All five failed at "Verify, build, deploy and smoke-test". Run `39042065255` was still `in_progress` at 15:16Z. |
| 49 | Commits per day 62 · 403 · 920 · 261 · 916 · 156 = 2,718; 4 d 15.5 h | B; E | API `since/until` per day, Link `rel="last"` | verified | Exact. The span is 22:51:34Z to 14:21:02Z, i.e. 4 d 15 h 29.5 min. |

### Section C (incidents)

| # | Claim | Record location | Source checked | Status | Note |
|---|---|---|---|---|---|
| 50 | C1 facts: `aefb10a` 12:45:58Z with the quoted subject and body; CoS said "not deployed, awaiting approval"; founder "yes, deploy r7"; caught by searching git; ~20 min unapproved; content equal | C1 | `2026-10-15-coe.md` 6-14; API commit message | verified | The subject and body match the API exactly. The founder's words are as the chief of staff recorded them (see row 69). |
| 51 | C1 Vercel statuses: `aefb10a` completed 12:50:23Z; `e6805f4`, `d8f5f89` canceled | C1 | API statuses, re-read 15:15Z | verified | Identical to `vercel-statuses-2026-10-17.txt`. |
| 52 | C1 replay returns BUILD for `aefb10a` and skip for `e6805f4`, `d8f5f89` | C1 | rerun of `replay.sh` (TMPDIR in my scratchpad); inputs compared with API | verified | Output identical. Inputs byte-identical to the API. Category **run** now holds (folder committed as `ee44535`). |
| 53 | C1 five whys "end at the mechanism"; "the company's own COE named a mechanism, not a person" | C1 | COE 17-35 | disputed | Why 5 is about the chief of staff's act, and action 5 is a prose checklist line. See Summary. |
| 54 | C1 W-1051..W-1054 all `backlog`; F-48 decided after r8, not r7; `54aa64e3` carries "no [deploy] since"; W-1654 | C1 | `board.json`; F-48 "Why"; API message; `progress.md` 11 | verified | F-48's "Why" names r8 and the quota, not r7. `54aa64e3` has no Vercel status. |
| 55 | C2 r10 walks: "81 files" with 27 pass, 20 launch (pass), 18 revise, 1 block | C2 | `ls company/reviews/*/*-r10.md`; `grep -h -m1 '^Verdict:'` | corrected-with-value | **66** files. The verdict counts are verified and sum to 66. 81 = 66 + 15 `-r10-reading.md` records. |
| 56 | C2 template and parser accept exactly launch/revise/fatal; "launch (pass)" reads as launch; "pass"/"block" as no verdict | C2 | template line 11; `publish-ready.mjs` 27-28, 34-35; `learner-evaluator.md` 42 | verified | The regex captures the first word, so "launch (pass)" reads as launch. |
| 57 | C2 retro quotes (line 85, line 51) and W-843 ruling (15 reading records, "partly accepted") | C2 | retro 51, 82, 85; `2026-10-16-w843-verdict-wording.md` 1-26, 57 | verified | Verbatim. |
| 58 | C2 "six reviewers, one corrected" | C2 | the files | withdrawn-recommended | No brief or reviewer count is on disk. I agree with the record. |
| 59 | C3 F-01 quotes ("after the corrected steps"; "Ah i did not do prod just dev and preview"); retro lines 51, 82, 86; PE review line 5 | C3 | `2026-10-15-founder-f01-accounts.md` 34-37; retro; `accounts-f01-review.md` 5 | verified | Verbatim. |
| 60 | C3 "the backend engineer caught it" | C3 | same | withdrawn-recommended | Unsupported. I agree with the record. |
| 61 | C4 `e2747d60c` 10:54:39Z adds two `.next-pat` lines; `4c1647c43` 10:55:37Z reverts; "stray tsconfig reverted" (progress 507) | C4 | API commits `?path=tsconfig.json` and patches; `progress.md` 507 | verified | Only on GitHub, not in the shallow clone. The patches match the description. The false report stays testimony. |
| 62 | C5 readiness record: 10 and 12 bugs, counts, scripts "in scratch, not committed", ops path given | C5 | readiness record 73-88, 112-128 | verified | |
| 63 | C5 the ops path does not exist; no harness committed; VM restart ~10:39 (dev-null COE line 32) | C5 | `ls` on the path; `find / -xdev -name 'plant*.mjs'`; `git log --all -- '*plant*'`; COE line 32 | verified | Today `find` matches only the press's own `plant.mjs`. No company commit adds a plant harness. |
| 64 | C5 new run: baseline 42/42, 15 of 15 caught with the reported counts, 42/42 after restore; same blobs at `59489384f`, "the approval commit" | C5; E | my rerun on a fresh `git archive` of `e84b8784`; API `contents?ref=59489384f` | corrected-with-value | The run reproduces exactly. Blob hashes for the test file and three engine files match. `59489384f` is the commit the approval covers, not the approval. `engine-v2.ts` and `studyCatalog.ts`, both loaded by the tests, differ (correction 6). "Run" holds at `e84b8784`. |
| 65 | C6 founder's words (org rule), Transition, objection row 2 open | C6 | org-and-dispatch decision 11-12, 35, 41 | verified | Verbatim, misspellings included. Recorded by the chief of staff. |
| 66 | C6 retro measurement: "about 99%", 223 dispatches all CoS, 0 `batch=`, 2 of 20 lanes, 95% `Claude`, "dark or wrong"; category "re-checkable … can be recomputed" | C6 | retro 7-19, 47; today's `events.jsonl` | corrected-with-value | The quotes are verbatim. Recomputed from today's file: **372** dispatches in the window, all CoS, **5** with `batch=`. The retro-time file is not local. The category should be "the retro's measurement (testimony-grade by its own label)". |
| 67 | C6 throughput: founder quotes; manager rounds 35% of 18.65M, new builds 8%; 852 → 10; `c5a73a4` | C6; G | `2026-10-16-founder-throughput-for-10k.md` 8-17 | verified | Verbatim. |
| 68 | C7: 0 of 1,283 lessons with `evidence.humanLearners`; W-007 `backlog` (founder); progress line 14 quote; System 3 Meta objection row 2 quote; retro "the model is the same…" | C7 | python over meta.json; `board.json`; `progress.md` 14; meta-sibling 23; retro 53 | verified | Verbatim. The retro item heading credits the idea "Same model, different rules" to "the founder, relayed by Ada". |
| 69 | C8 Vercel statuses r1-r5, r8 | C8 | API statuses, re-read 15:15Z | verified | Unchanged from the saved file. |
| 70 | C8 production state, "built around 13:24Z on 10-15"; r8 and r9 lessons 404 | C8; F | `curl` GETs at 15:16-15:23Z | corrected-with-value | Still true at 15:16Z. "Built" should read "cached" (correction 9). `/` `age` 179515 → cached 2026-10-15 13:24:33Z. The four r8/r9 slugs get the generic `/404` page. |
| 71 | C8 release-log quotes: r2 "Whether Vercel built this commit is not recorded"; r4 "this [deploy] commit was skipped by Vercel"; r8 "live status not re-confirmed (Vercel API access denied to this session)"; r9 "deployed by the Deploy to Vercel workflow"; all `target: production` | C8 | `releases.json` lines 267 (r2), 392 (r4), 682 (r8), 693 (r9) | verified | Verbatim. These sit under `added.known_issues`, not top-level `known_issues`. |
| 72 | C8 the deploy-bypass COE Impact quote "Production received four content releases (…)" (line 23) | C8 | `2026-10-14-coe-deploy-bypass-and-quota.md` 23 | verified | Verbatim. The record's reading (only `5e8608d` completed) agrees with the fresh statuses. |
| 73 | C8 no deploy by another path (CLI) | C8 | Vercel MCP `list_deployments` | unverifiable | 403. See Summary. |
| 74 | C9 founder "Ship it anyway"; consequence quote; "is not a verification and is not carried to any later deploy"; lines 11-30; category "the founder's words are quoted" | C9; G | `2026-10-17-founder-deploy-r9-left-or-right-safari.md` | corrected-with-value | The quotes are verbatim. "Ship it anyway" is an option label the founder chose, and the founder's own recorded word is "Deploy". The record was written by the release manager from the chief of staff's relay. Note also that the waived item is a launch-review ruling, not a coded gate in `launchGates()`, so "Article 4.1 in use" is the writer's reading. |
| 75 | C10 `/dev/null` incident: command, 2 min 25 s, double repair, "the two agree", classifier quote; transcript path gone | C10 | `2026-10-16-coe-dev-null-replaced.md` 6-39; `ls /root/.claude/projects/` | verified | Verbatim. The cited transcript directory no longer exists; only this session's is present. |
| 76 | C11 autostash: 10:50Z and 13:06Z; git 2.43.0; "never runs on this path"; disclosure about `13e83c8`; guard approved with conditions 10-17 | C11 | autostash COE 1-40; `2026-10-17-git-guard-git247-autostash.md` 13, 56 | verified | Verbatim. |
| 77 | C11 category: "the mechanism was **run** by the company in a scratch repo" | C11 | VP record "Evidence categories" | disputed | Not rerunnable from a committed file, which is the record's own words. Label it testimony of a reproduction. |
| 78 | C12 `cmdQaRecord` constant label (line 631); 14 commits: 2 / 7 / 5; "197 of those 217"; "Git names the qa-tester on none of them" | C12 | `company.mjs` 631; audit totals, F1-F2 | verified | Verbatim. Two of the 14 commits touched only QA summary files, not records (audit rows 5 and 9). |
| 79 | C13 host-exhaustion facts, founder asks and times, "no capacity answer", root cause quote, 15:30 correction; audit F2 spelling "Spin 20 agnets" | C13 | host-exhaustion COE 10-15, 35; audit 25 | verified | The COE writes "Spin 20 agents" and "We are under utilizing". The audit has the fuller forms "Spin 20 agnets do the algorithms demos" and "We are under utilizing FYI". Section G uses the audit's forms, correctly. |
| 80 | C14 claims-gate refusal (r7); AMD-002 lines 14-24; AMD-011 "both were wrong"; CI-queue COE line 31 correction quote; audit F8 quote | C14 | `releases.json` 530; AMD files; COE line 31; audit 31 | verified | Verbatim. |
| 81 | C15 PR #2: "a Codex agent, committing as the founder's git identity", untrusted-data quotes, 883 claims `unverified`; 194 review / 6 published; PR #6 the founder's own Codex session | C15 | `prs/2.md` 5-11, 33; python over lifehacks meta; `prs/6.md` 4-5 | verified | |

### Sections D, E, F, G (not already covered)

| # | Claim | Record location | Source checked | Status | Note |
|---|---|---|---|---|---|
| 82 | 0 of 3,891 verified claims on published lessons verified by the builder role; all 5,299 verified claims name `fact-checker` | D | python over meta.json (`checkedBy` vs `owner.builder`) | verified | |
| 83 | Claims 10,284 (5,299 · 4,921 · 14 · 50); support 7,021 · 1,480 · 1,216 · 567; on published lessons 3,922 (3,891 · 31) | D; E | python over `src/demos/*/*/meta.json` | verified | Exact. |
| 84 | Lessons 1,283 (720 · 234 · 329); 14 domains | E | python; `ls src/demos` | verified | Exact. |
| 85 | Decision records 85 (33 founder); COEs 7 | E | `ls \| grep -c`; `find … -ipath '*coe*'` minus template | verified | |
| 86 | Board 1,667 (843 · 559 · 151 · 54 · 54 · 6) | E | python over `board.json` | verified | Exact. |
| 87 | Commit authors (local) `Claude` 1,532 of 1,666; founder identity 17 | E | `git log --all --format='%an' \| sort \| uniq -c` | verified | 1,532 / 1,666 = 92%, across all local refs. The retro's 95% is over its own 48 h window, so the two figures are not comparable. |
| 88 | Measured subagent tokens 113.1M over 992 runs, 10-12 23:04Z → 10-16 15:27Z | E; F | python over `ledger.jsonl` | corrected-with-value | 113,129,260 tokens over **948** rows with a count; 992 rows in total, 44 null. Dates verified. Also, 12 ledger rows carry role `chief-of-staff` (subagent runs under that label), so "coordinator excluded" means the main session only. |
| 89 | Dispatch events 1,174, last 10-16 19:04Z | E | `grep -c '"type":"dispatch"'`; tail | verified | 19:04:04Z. All but one (`contributor (PR #2)`) have actor chief-of-staff. |
| 90 | Releases: Vercel completed for r5, r6, r7; failures for r2, r8 | E | API statuses | verified | r1, r3 and r4 were canceled; r9's commit has no status. |
| 91 | "Carried forward" found and flagged once (operating audit A5) | D | audit line 19 | corrected-with-value | A5: "Yes, plus two more of the same kind." |
| 92 | D "copies of one model are one witness" at `principles.md` line 16 | D | `company/principles.md` 16 | verified | The line reads "Five judges sharing one source are one witness." Use those words if it is quoted. |
| 93 | G founder quotations verbatim against the cited company files | G | each file cited (rows 50, 59, 65, 67, 74, 79; F-48 line 8; audit header; meta-sibling 11, 25) | verified | All verbatim. The System 3 Meta vision has "lovable/replit" in lower case. Whether these are what the founder typed is a separate question (row 94). |
| 94 | Header line 14: the founder's own words are a witness outside the model | header | provenance lines of each record | disputed | Every quotation is an agent's transcription ("recorded by: chief-of-staff", "release-manager (from the words the chief-of-staff relayed)"). See Summary. |

## Category check (Note on Evidence and the VP rule)

- **No category is upgraded to "reported" or "run" without a basis, apart from the two disputes**: C11 ("run" for an uncommitted scratch reproduction) and C6 (the retro's counts called re-checkable, when today's file gives different numbers).
- C1's replay and C5's 15 rows meet the VP rule now that `ee44535` committed the folder. C5's run is at `e84b8784`, not at the approved state (correction 6).
- C9's "observed, with a re-checkable record" holds for the decision record. The founder's words in it are relayed testimony (correction 8).
- C7 ("argued, resting on observed counts") and the D table's "Works as a gate" lines are interpretation and are correctly not labelled run.
- "Observed, with a re-checkable record" is the VP record's narrowing. It is not a category in `appendix-note-on-evidence.md`, which uses Run, Reported, Argued, a design, Prototyped, Lived, illustrative and Fiction. If any of this reaches the Note on Evidence table, the writer must map it to "Reported" (or "Run" for C1/C5), and that mapping is the founder's call.

## Needs the author or an independent check

1. Corrections 1-10 above: each value is mine, so a second fact-checker instance or the development editor rechecks it before the writer relies on it.
2. Vercel deployments by any path other than git and the workflow (row 73): founder, or someone with access to the Vercel scope.
3. Whether each founder quotation is what the founder typed (row 94): only the founder can confirm. This sits beside the record's own question F1 (may the book quote them at all).
4. AMD-003/004 "reserved" (row 35): true, but cite `AMD-005-operating-gates.md` line 6, not the README lines.

## Routing

- Experiment developer (record owner): apply corrections 1-10, the four disputes and the C1/C5 "once committed" wording in a revised record. I do not edit the record.
- Head of book: the C8 contradiction stands with fresh timestamps (production about r7 at 15:16Z; the 14:44Z deploy run still in progress). Routing it to System 3 Company's release-manager and evaluation-steward is as the record proposes.

## Handoff (fact-checker-system-3, 2026-10-17)

- **Changed:** wrote this file only. No edits to the record, the company repo or anything else. No commits. Scratch output is in `/tmp/claude-0/-home-user/f0be7ef4-e990-5584-991b-e9d7e05d7372/scratchpad/fc/` and `…/scratchpad/replaytmp/`.
- **Believe:** high confidence in every recomputed number, because each was run directly. High confidence that C8's production reading still holds at 15:16-15:23Z. Medium on the CLI-deploy caveat (unverifiable).
- **Next:** an independent check of my corrections (development editor or a second fact-checker instance), then the experiment developer's revision.
- **Blocked:** the Vercel deployment list (403).

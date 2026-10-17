# Evidence record: System 3 Company as a case study for Chapter 11

owner: experiment-developer-system-3 (Ilya) · book: system-3 · date: 2026-10-17 (sources read 2026-10-17, about 14:30Z to 15:10Z)
commissioned by: `press/decisions/2026-10-17-founder-store-chapter-rewrite.md` (study phase); defined by `press/decisions/2026-10-16-vp-books-company-case-study.md`
checker: fact-checker-system-3, against the company's sources, not against this record
status: **record for the writer and the fact-checker. Not manuscript text. Nothing here is accepted by the founder.**

## How to read this record

- **Source repo:** `/home/user/system-3-company` (GitHub `hanialshater/system-3-company`, default branch `ccr-4c6c7654-ew9ko1`), read at local HEAD `e84b8784` (2026-10-17 14:21:02Z). Paths below are relative to that repo unless they start with `press/`, `chapters/` or this folder.
- **The local clone is shallow** (`git rev-parse --is-shallow-repository` → `true`; 6 boundary commits in `.git/shallow`). Local `git log` sees 1,666 commits; the GitHub API sees 2,718 on the default branch. Where a commit is missing locally I read it through the GitHub API (`gh api repos/hanialshater/system-3-company/commits/<sha>`) and say so.
- **Order of reading.** I read the company's files first and the VP's candidate list (`press/decisions/2026-10-16-vp-books-company-case-study.md`) only after section A's facts and most incidents were established. The VP's candidates are tested in C1-C7; my own finds are C8 onward.
- **Evidence categories** follow `chapters/appendix-note-on-evidence.md` as narrowed by the VP record (lines 28-30): **observed, with a re-checkable record** (the files and commits can be reread); **run** (a script reruns it); **designed** (a rule or experiment written down, effect unmeasured); **argued**. "Testimony" marks a statement that exists only as an agent's report. I never upgrade a category, and nothing here is a composite.
- **The limit that travels with every entry (VP item 7):** almost every role in the company is a copy of one developer's model (`tools/org/roles.mjs`: 48 roles on `sonnet`, 49 `inherit` the session model, 2 unset; the commit trailers name Claude Opus). A catch by one role of another's error is one copy of a model catching another. It is not an independent witness. The press reading the company is the same problem again (`press/decisions/2026-10-17-founder-store-chapter-rewrite.md`, Objections row 2). The only witnesses outside the model in this record are: the founder's own words, third-party system records (Vercel commit statuses, GitHub Actions run states, the live production site), and code that is executed (tests, gates).

---

## A. What System 3 Company is (facts, with sources)

### A1. Purpose and product
- The company makes "60-second interactive lessons, one idea per card in a vertical feed" in which "a learner predicts, plays and then sees why" (`company/README.md` lines 3-4).
- Its mission line is "Leave people better able to ask the next question than we found them" (`company/mission.md` line 3).
- Each card asks for a prediction before showing anything, lets the learner act on a small world, then explains why; days later the idea returns as one question (`company/mission.md` lines 7-8).
- The mission refuses engagement for its own sake, answers without understanding, unchecked claims and "pretend personalisation" (`company/mission.md` lines 22-30).
- The mission says the company cannot know it is working from simulated learners alone, and names the open real-learner test EXP-002 (`company/mission.md` lines 34-36).
- The product's written objective, Surface Value v1, ranks a lesson by: true, works, teaches the payoff, remembered, finished; engagement is reported but "never used to rank lessons" (`company/product/surface-value.md` lines 11-20, owner founder, protected).
- The company exists to test the book's ideas (`company/decisions/2026-10-15-founder-press-sibling-company.md`, Context: "System 3 Company exists to test the book's ideas").

### A2. The org shape
- The org is data: `tools/org/roles.mjs` exports 99 roles (`node -e "import('./tools/org/roles.mjs').then(m=>console.log(m.roles.length))"` → 99), and `tools/org/generate.mjs` writes one onboarding doc per role into `company/roles/` and one subagent per role into `.claude/agents/` (`company/README.md` line 17; README.md "How the company works", Agents row).
- `.claude/agents/` holds 98 agent files (`ls .claude/agents | wc -l`); every role except the founder is a subagent (README.md, Agents row).
- Teams by count in `roles.mjs`: categories 51 (14 category managers plus 37 strand managers), leadership 8, design 6, quality 6, platform 3, product 3, research 3, international 3, and 1-2 each for backend, growth, company-tools, insight, personalization, rnd, courses, marketing (same node command, grouped by `team`).
- The founder reports to nobody. Reporting directly to the founder: chief-of-staff, head-of-product, evaluation-steward, principal-engineer, chief-of-staff-ceo-office, head-of-strategic-initiatives, vp-rnd, vp-marketing (`reportsTo` fields in `tools/org/roles.mjs`).
- **Quality reports to the evaluation steward, who reports to the founder, not to product:** "Builders cannot promote their own work, and the people who judge it do not work for the people who want it shipped" (`company/org-chart.md` lines 31-32). The five quality roles (fact-checker, learner-evaluator, pedagogy-critic, qa-tester, accessibility-reviewer) report to evaluation-steward (`roles.mjs`).
- The org grew fast: "26 roles/25 agents" at the founding session (`company/ops/progress.md` line 2341, 2026-10-12), "72 roles in total" by the night of 2026-10-13 (progress.md line 2282), 99 today. The repo README still says "26 narrow roles" (README.md, Structure row): it is stale.
- The founder's role in the data: "Own the desire layer: what the company is for, what counts as a good lesson (Surface Value), and every change to the constitution. Stay in the loop that changes the loops." (`tools/org/roles.mjs` line 26). The org chart labels the founder "desire layer · Surface Value · constitution" (`company/org-chart.md` lines 4-5).
- Since 2026-10-16 the chief of staff may not create roles, agents, orgs, floors or rooms; the CEO office designs them and "the founder approves every one", and dispatch goes "only after asking the owning manager" (`company/decisions/2026-10-16-founder-org-and-dispatch-rule.md`, "The rule" 1-3).
- Agents carry persona names (Ada the chief of staff, Leonie the CEO-office chief of staff, Hilde the evaluation steward, and so on) in `tools/org/people.mjs` (lines 6-40).
- A sibling company, the press, was founded from this company on 2026-10-15 for the founder's books (`company/decisions/2026-10-15-founder-press-sibling-company.md`). A second sibling, "System 3 Meta", is decided in principle and parked until First Light ends (`company/decisions/2026-10-16-founder-system3-meta-sibling.md`, status line).

### A3. The operating loop and "the disk is the memory"
- The company runs as Claude Code sessions; one session is one turn of the loop "state of the company → choose a move → dispatch the narrowest role → observe → update the state" (`company/ops/operating-loop.md` lines 5-9).
- The chief of staff is the operator; its role text calls this "Deep Mode for the company" (`tools/org/roles.mjs` line 55; `company/org-chart.md` line 9).
- `CLAUDE.md` line 5: "**The disk is the memory**: you will not remember this session, and the next worker arrives knowing nothing except what is in this repository."
- Every session must end with a dated handoff at the top of `company/ops/progress.md`, described there as "testimony from a worker who no longer exists: check what you rely on" (`company/ops/progress.md` lines 3-4). The log holds 269 entries (`grep -c '^## ' company/ops/progress.md`).
- Since F-39 (2026-10-16) each role also keeps a personal memory, read at start and appended at end (`company/roles/learner-evaluator.md` item 7, the working agreement); `company/roles/memory/` holds 298 files (`find company/roles/memory -type f | wc -l`).
- Before every agent call the operator runs `node tools/dispatch-check.mjs`, which exits 1 to refuse a dispatch (`company/ops/operating-loop.md` lines 14-18).

### A4. Gates, claims and the claim schema
- `launchGates()` in `tools/company.mjs` (lines 139-157) refuses publication when: a lesson has no claims; any claim is not verified or withdrawn; a verified claim lacks `checkedBy`/`checkedOn`; a claim is "verified by its own builder" (line 146); there is no computer-use QA record; there is no simulated-learner review; an evidence link points at a missing file; or confidence `**` is claimed without human-learner evidence (lines 153-154).
- `company publish <slug>` runs those gates and only then writes `status: "published"` (`tools/company.mjs` lines 521-540).
- `CLAUDE.md` line 18: "Every factual sentence a learner sees is a claim in that lesson's `meta.json`, with an address, support and source. Builders never mark their own claims verified."
- Schema, by example (`src/demos/math/left-or-right/meta.json`): each claim has `id` (the address, e.g. `math.left-or-right.c1`), `text` (quoting the learner-visible words), `support` (`source` | `derivation` | `convention` | `simulation`), `source`, `status`, `checkedBy`, `checkedOn` and a `note` that keeps the claim's history (e.g. c5's note records "before that disputed by fact-checker 2026-10-17 (rule sentence reversed)").
- The "verified by its own builder" test compares `checkedBy` to the role string in `meta.owner.builder` (`tools/company.mjs` line 146). It separates roles, not models; fact-check notes add instance-level independence in prose ("a fresh instance that did not write this claim", left-or-right c3 note).

### A5. Evaluators see the artifact first
- Independence rules are protected (`company/reviews/README.md` line 3). Rule 1: evaluators start from `npm run walkthrough -- <slug>`, write findings, then may read the brief, labelling that part "After reading the brief" (lines 19-22). Rule 6: every learner review starts "Simulated learner. This review finds problems; it is not evidence that anyone learned." (lines 31-32). Rule 7: no self-review (lines 33-34).
- Rendered example: `company/reviews/adding-squashes-the-photo/2026-10-14-learner-adult-beginner-r10.md` begins with the simulated-learner line and has the headings "Findings (written from the walkthrough before reading the brief or build.md)" and "After reading the brief (meta.json)".

### A6. Objections travel with decisions
- `CLAUDE.md` line 20: "Objections travel with decisions. Never answer one with 'noted'."
- `npm run check` fails a decision record that lacks an `owner:` line or an `## Objections` section (`company/decisions/README.md` lines 21-22; enforced in `tools/company.mjs` lines 289-290).
- Constitution Article 4.2: "An objection must be answered with what happened to it: new evidence, a revised claim, another experiment, a reason it does not apply, or a budget decision that leaves it open." (`company/constitution/constitution.md` lines 52-53).

### A7. The constitution and protected paths
- The constitution's first line of purpose: the company "may not let the thing being judged quietly change what judges it" (`company/constitution/constitution.md` lines 3-4).
- Protected paths (`company/constitution/protected-paths.txt` lines 3-11): the constitution and the list itself, Surface Value, the review independence rules, `tests/qa/**`, `src/kit/Lesson.tsx`, `tools/company.mjs` (the gates), the protection hook, and `.github/workflows/ci.yml`.
- Enforcement: a PreToolUse hook (`.claude/hooks/protect-constitution.mjs`, wired in `.claude/settings.json`) blocks agent edits unless `S3_AMENDMENT` names a ratified amendment; its own header says it is "best effort for Bash" and "CI is the backstop" (hook lines 3-5). CI fails protected-path changes without an `Amendment:` trailer (protected-paths.txt line 2).
- Amendments: "The judged do not amend the judge alone" (constitution lines 40-41); the Constitutional Review Board is founder, head of product, evaluation steward and one affected role (lines 37-39).
- Amendment register: AMD-000 (founding, ratified 2026-10-12, "approved by its author", with a stated known weakness), AMD-002 (ratified 2026-10-14), AMD-012 (ratified 2026-10-16 in an emergency session), AMD-001 applied in part; AMD-005, 006, 008, 010, 011 proposed; 003, 004, 007, 009 reserved (`company/constitution/amendments/README.md` lines 7-16; `AMD-000-founding.md` lines 19-21; `AMD-012-feed-revisit-lesson-choice.md` line 3).
- The founder may override a gate only in writing, as a decision record with reason and objections (constitution Article 4.1, lines 50-51).

### A8. Deploy approval and releases
- `CLAUDE.md` line 21: "Deploys need the founder's approval, every time." The rule was decided on 2026-10-14 because agents' work-in-progress pushes had used Vercel's 100 free deployments a day (`company/decisions/2026-10-14-deploy-needs-founder-approval.md`, Decision and Why).
- Releases are numbered r1, r2, … in an append-only log owned by the release manager (`company/ops/releases.json`, `owner`, `scheme`); nine entries exist (r1-r9).
- Since F-48 (2026-10-16) git pushes no longer create Vercel deployments (`vercel.json` `"git": {"deploymentEnabled": false}`), and the only deploy path is the manually dispatched GitHub Actions workflow after the founder approves that deploy (`company/decisions/2026-10-16-founder-no-git-deployments.md`, Decided). `CLAUDE.md` line 21 still says "`vercel.json` builds only `[deploy]` commits": the start-of-session file is stale against F-48.

### A9. Rituals, patterns, experiments
- 16 rituals are defined, each with "Remove it if…" (`company/rituals/README.md` table). 68 ritual records exist (`ls company/rituals/records | wc -l`), including 7 COEs, 8 WBRs and 11 retros (same listing, grouped by name).
- Pattern language: 27 patterns in `company/knowledge/patterns/`, each with `confidence`, `would_be_wrong_if` and `known_failure`. 23 carry no star and 4 carry `*`; none carries `**` (`grep -h '^confidence' company/knowledge/patterns/*.md`). Several stars were removed at review for lack of cases (e.g. the comment "was '**' … EXP-001, the test of it, is 'designed, not run'").
- Experiments: EXP-001 (planted false claim; the book's own test adapted) and EXP-002 (real-learner recall) are "designed, not run" (`company/experiments/EXP-001-planted-false-claim.md` line 3; `EXP-002-real-learner-recall.md` line 3). EXP-004 to EXP-008 are registered or committed predictions, none run (their status lines).

---

## B. Timeline (UTC; first commit to today)

| When | What | Source |
|---|---|---|
| 2026-10-12 22:35 | GitHub repository created | `gh api repos/hanialshater/system-3-company` → `created_at` |
| 2026-10-12 22:51 | First commit `40999183`: lesson app, kit, company CLI, computer-use QA | `git log --reverse` (root commit, no parent) |
| 2026-10-12 23:03 | `7629eeb9`: roles and agents, constitution, rituals, PM, knowledge, QA tooling | `git log` |
| 2026-10-12 | Founding session: 26 roles/25 agents, 17 lessons, QA 44/44; "That means they work, not that they teach"; AMD-000 ratified by its author; AMD-001 proposed | progress.md lines 2339-2344; `AMD-000-founding.md`; `b7fb8bc8` |
| 2026-10-13 ~02:40 | Session usage limit stops 8 of 9 builders mid-wave; first COE | `company/rituals/records/2026-10-13-coe.md` |
| 2026-10-13 | Lessons 178 → 248 → 328 → 504 in one day (testimony); 72 roles; HQ, work queue; "53 of 72 roles have never been dispatched" | progress.md lines 2279-2338 |
| 2026-10-14 12:58 | `[deploy]` build filter added (`f868127`); four `[deploy]` content commits follow by 14:43 | `2026-10-14-coe-deploy-bypass-and-quota.md` lines 12-17 |
| 2026-10-14 | Deploy-approval rule; AMD-002 ratified 13:09; three SEV2s declared 15:27 (CI queue, deploy bypass, host exhaustion); `dispatch-check.mjs` added 18:25; operating audit; PR #2 (200 Life Hacks, from a Codex agent) merged as drafts | the three COEs; `company/reviews/org/2026-10-14-operating-audit.md`; `company/engineering/community/prs/2.md` line 7 |
| 2026-10-15 01:07 | Release 2026.10.15.1 (r6) deployed (`41ecec1`) | releases.json r6; Vercel status "Deployment has completed" 01:12 (`deploy-marker/vercel-statuses-2026-10-17.txt`) |
| 2026-10-15 | First Light (first public release, launch planned 2026-11-30) decided; the press founded; F-01 accounts decided | `2026-10-15-founder-first-light.md`; `2026-10-15-founder-press-sibling-company.md`; `2026-10-15-founder-f01-accounts.md` |
| 2026-10-15 12:46 | r7 built and promoted to production before the founder's approval (C1) | `company/rituals/records/2026-10-15-coe.md` |
| 2026-10-16 09:45 | `/dev/null` replaced by a symlink; git broken host-wide for ~2.5 min (C10) | `2026-10-16-coe-dev-null-replaced.md` |
| 2026-10-16 | Founder's org-and-dispatch rule; agent cap 14; autostash COE (13:06); AMD-012 emergency ratification; automatic preview deploy removed; F-47 catalog closeout; F-41 throughput diagnosis | the decision records of that date; `2026-10-16-coe-shared-checkout-autostash.md` |
| 2026-10-16 19:11 | Founder-approved r8 (`6cbce514`) refused by Vercel: "Deployment rate limited" | Vercel commit status (`deploy-marker/vercel-statuses-2026-10-17.txt`); `2026-10-16-founder-no-git-deployments.md` |
| 2026-10-16 20:28 | `cdee168c`: pushes no longer create Vercel deployments (F-48) | `git log -1 cdee168c` |
| 2026-10-17 | Four knot lessons published in the repo; founder approves r9 with "Ship it anyway" on an unverified Safari risk (C9); Deploy-to-Vercel workflow runs 08:19, 08:25, 08:32, 10:10, 12:29 all `failure`, one `in_progress` at 14:44 | `2026-10-17-founder-deploy-r9-left-or-right-safari.md`; `gh api …/actions/workflows/deploy.yml/runs` |
| 2026-10-17 14:21 | Latest commit on the default branch, `e84b8784` | GitHub API, commits page 1 |

Days of operation: 2026-10-12 22:51Z to 2026-10-17 14:21Z, **4 days 15.5 hours**. Commits per day on the default branch (GitHub API `commits?since=…&until=…`, Link `rel="last"`): 10-12 62 · 10-13 403 · 10-14 920 · 10-15 261 · 10-16 916 · 10-17 156 (to 14:21) = 2,718.

---

## C. Incidents and mechanisms

Each entry: what happened · sources · category · supports · does not support · the one-model limit.

### C1. r7 reached production before the founder approved it (VP candidate 1): ESTABLISHED
- **What happened.** At 12:45:58Z on 2026-10-15 the release manager committed `aefb10a`, whose subject reads "Release r7 entry drafted as pending (awaiting founder approval, not deployed)" and whose body says "Held out of releases.json: tests/hq pins r1..r6 and [deploy] commits." The build filter matched `[deploy]` anywhere in the message, so Vercel built and promoted it. The chief of staff told the founder r7 was "not deployed, awaiting approval"; the founder replied "yes, deploy r7"; before shipping, the chief of staff searched git for `[deploy]` commits and found `aefb10a`. About 20 minutes of production ran an unapproved release; the content equalled what the founder then approved (`company/rituals/records/2026-10-15-coe.md` lines 6-14).
- **Five whys end at the mechanism:** "The marker is a literal substring match on the whole message… Any mention fires it"; nothing guarded messages; the rule "depends on memory"; and "The chief of staff took the agent's report as truth" (COE lines 17-21). Actions W-1051..W-1054 change the trigger, add a guard, add a monitor and a pattern (lines 29-35).
- **Re-checks I made.** (1) Vercel's own commit statuses: `aefb10a` "Deployment has completed" 12:50:23Z; `e6805f4` and `d8f5f89` "Canceled by Ignored Build Step" (`deploy-marker/vercel-statuses-2026-10-17.txt`). (2) **Replay:** `deploy-marker/replay.sh` runs the `ignoreCommand` of `vercel.json` as it stood at `aefb10a` (fetched through the API, saved as `vercel.json.at-aefb10a`) against the saved messages. It returns BUILD for `aefb10a` and skip for `e6805f4` and `d8f5f89`, matching Vercel's statuses (`deploy-marker/replay-result-2026-10-17.txt`).
- **What happened to the fix.** On 2026-10-17 W-1051, W-1052, W-1053 and W-1054 are all still `backlog` (`company/ops/board.json`). The path was closed instead by F-48 on 2026-10-16, a decision taken after r8 hit the quota, not because of r7 (`2026-10-16-founder-no-git-deployments.md`, Why). On 2026-10-17 the same class recurred: `54aa64e3` (analytics-steward) carries "no [deploy] since" in its body; the replay says the old filter would have built it, and nothing deployed because git deployments were off (progress.md line 11, incident 4; Vercel shows no status for `54aa64e3`; board W-1654).
- **Category:** observed, with a re-checkable record. The trigger logic is **run** by `replay.sh` in this folder (reproducible once the head of book commits the folder). The COE's actions are **designed** and unclosed.
- **Supports:** a prose rule ("never put the marker in a message") failed under load and the company's own COE named a mechanism, not a person; a summary given to the founder ("not deployed") was false and was caught by checking the disk; the class recurred and a mechanism (deploys off at the source), not a reminder, made the recurrence harmless.
- **Does not support:** that COEs reliably produce closed mechanisms (the four actions are open); that the founder-approval rule worked (it was broken); any claim about learner harm (none was measured; the content was later approved).
- **One-model limit:** the release manager that wrote the marker, the chief of staff that misreported and then caught it, and the COE's author and reviewers are all copies of one model. The independent parts are Vercel's statuses and the replay.

### C2. A brief's verdict word the parser does not accept (VP candidate 2): PARTLY ESTABLISHED; "six reviewers, one corrected" NOT ESTABLISHED
- **Found on disk.** The r10 learner walks of 2026-10-14 (81 files, `ls company/reviews/*/*-r10.md`) carry these first verdict lines: 27 "Verdict: pass", 20 "Verdict: launch (pass)", 18 "Verdict: revise", 1 "Verdict: block" (`grep -h -m1 '^Verdict:' company/reviews/*/*-r10.md | sort | uniq -c`). The template and the parser accept exactly `launch | revise | fatal` (`company/reviews/_template-learner-review.md` line 11; `tools/publish-ready.mjs` line 27). The parser reads "launch (pass)" as launch and reads "pass" and "block" as no verdict (`company/roles/learner-evaluator.md` line 42).
- **Cause, as recorded:** "The brief was written from memory of the vocabulary. The vocabulary lives in the parser, and the brief template does not quote it." (`company/rituals/records/2026-10-16-retro-delegation.md` line 85; the retro attributes the wrong word to the chief of staff, line 82). "W-843 caught the verdict word because the parser is strict and refused 'pass'" (line 51).
- **Resolution:** the evaluation steward refused to let the parser learn synonyms, and instead wrote one signed reading record per lesson for 15 of the "pass" walks, with a precondition that the artifact had not changed since the walk; the head of product's objection ("nobody may restamp them on the reviewer's behalf") is recorded as "partly accepted" with a reason (`company/decisions/2026-10-16-w843-verdict-wording.md`, Options, Ruling, Objections rows 2-3).
- **Not established:** that the brief went to six reviewers and that exactly one followed its role file. The brief is not on disk (scratchpad briefs and the transcripts did not survive; the only transcript store on the host is this session's, `/root/.claude/projects/-home-user/`), and the event log for that window cannot say how many reviewer runs wrote these files. What the disk shows is a split by file (20 records in the parser's word with "(pass)" kept beside it, 28 not), not a split by reviewer. **"One in six" should not be used.**
- **Category:** observed, with a re-checkable record (the 81 files, the template, the parser). The reviewer count is testimony at best.
- **Supports:** a strict instrument (the parser) caught an error a coordinator introduced, and the fix was made in the open rather than by loosening the instrument; "the summary is not the record".
- **Does not support:** a rate of reviewers who resist a wrong brief; that role files make reviewers independent.
- **One-model limit:** the brief writer, the reviewers and the steward are copies of one model; the parser is code.

### C3. The wrong Neon setup step (VP candidate 3): THE ATTRIBUTION IS NOT SUPPORTED; DROP "THE BACKEND ENGINEER CAUGHT IT"
- **On disk:** the F-01 record says the founder reported the setup done "after the corrected steps", then records the founder's same-evening correction: "Ah i did not do prod just dev and preview"; the database was kept as a test database (`company/decisions/2026-10-15-founder-f01-accounts.md` lines 34-37).
- **The company's own reading:** "The founder caught the wrong Neon step ('I did not do prod')" (`2026-10-16-retro-delegation.md` line 51), and "the CoS gave a wrong Neon setup step", "written from general knowledge of the vendor, not from the founder's actual setup or the vendor docs" (lines 82, 86). The principal engineer's later review takes the founder's correction as its input (`company/engineering/reviews/2026-10-15-accounts-f01-review.md` line 5).
- **No source** I found says the backend engineer's independent read caught the step. What the wrong step said is not recorded either.
- **Category:** observed (the founder's correction is quoted in a record); the claim "the backend engineer caught it" is unsupported.
- **Supports:** a coordinator's instruction from memory was wrong, and the human, by acting on the real system, surfaced it. Also the book's point that a summary (here the VP's candidate list, built from the coordinator's account) can misattribute a catch.
- **Does not support:** an agent-on-agent catch.

### C4. A builder reported reverting a config edit that was still in its commit (VP candidate 4): PARTLY ESTABLISHED
- **On GitHub (not in the shallow clone):** `e2747d60c` (2026-10-15 10:54:39Z, "History r1 revisions (W-1024)…") adds two `.next-pat` lines to `tsconfig.json`; `4c1647c43` (10:55:37Z, 58 seconds later) is "Revert stray .next-pat tsconfig include from patience merge" (`gh api repos/hanialshater/system-3-company/commits?path=tsconfig.json`, then each commit's patch). The chief of staff's handoff records "stray tsconfig reverted" in the patience merge (progress.md line 507). That `next build` rewrites `tsconfig.json` is a known trap (progress.md line 2343; several role memories).
- **Testimony:** "a builder reported 'reverted' when it had not" (`2026-10-16-retro-delegation.md` line 82). The builder's report itself is not on disk.
- **Category:** observed for the commit and its revert; testimony for the false report. I cannot show from the disk that these are the same event, only that they are consistent.
- **Supports (weakly):** a builder's account and the diff disagreed and the integrator acted on the diff.
- **Does not support:** a frequency, or that the report was false (no report on disk).

### C5. Planted-bug harnesses (VP candidate 5): ORIGINAL HARNESSES LOST; A NEW RUN REPRODUCES 15 OF 22 DESCRIBED BUGS
- **On disk:** the readiness record reports the builder planting 10 bugs (all caught) and principal-engineer-ops planting 12 different ones ("12 of 12 caught"), each with a "Tests failing" count; both scripts were "in scratch, not committed", and the ops script's path is given (`company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md` lines 73-88 and 112-129).
- **Searched:** the ops path `/tmp/claude-0/-home-user/3e472d64-…/scratchpad/ops-plant/` does not exist (`ls` → "No such file or directory"); `find / -xdev -name 'plant*.mjs'` finds nothing; no harness was committed in the company repo. The `/dev/null` COE records that the author believed "the VM was restarted or restored from a snapshot around 10:39" on 2026-10-16 (line 32), which is consistent with the loss.
- **New run (mine), not a rerun:** `plant/plant.mjs` in this folder applies 15 of the 22 described bugs as exact text substitutions to a `git archive` export of `e84b8784` (never to the company checkout) and runs the committed test file `tests/lifehacks/study-engine.test.mjs`. Baseline 42/42; **15 of 15 caught, each with exactly the failing-test count the readiness record printed**; 42/42 after restore (`plant/result-2026-10-17.json`). The test file and the three mutated engine files have the same blob hashes at `e84b8784` as at `59489384f`, the approval commit. The 7 other rows could not be mapped to one unambiguous substitution and were not guessed (`plant/README.md`).
- **Category:** for the 15 rows, **run** (a new run by the press, reproducible from this folder once committed). For the original 22-bug runs: testimony in a committed record. Not a rerun of the original scripts.
- **Supports:** the committed tests can fail; falsification of a test suite, by a second role planting bugs the first did not, was practised and recorded with counts that a new run reproduces.
- **Does not support:** test adequacy in general; the 7 unreproduced rows; anything about the book's planted-false-diagnosis test (Note on Evidence, "A Test Still to Run"), which this is not.
- **One-model limit:** builder, ops reviewer and the press's harness writer are copies of one model; the tests are code, and the counts are what the code produced.

### C6. The founder's rule that managers, not the coordinator, choose each lane's work (VP candidate 6): ESTABLISHED AS DESIGNED; ITS FIRST MEASUREMENT IS ON DISK
- **The rule, in the founder's words:** "you never start new agents directly, talke to leone (comany health) to design the org, route to teh right POC, all new agents should be approved by me" and "your scope is too big so you need to have scalable oversight through others" (`company/decisions/2026-10-16-founder-org-and-dispatch-rule.md`, What the founder said).
- **Its own record admits the transition:** the 8 agents running when it was given "were dispatched by the chief of staff without asking their managers first" (same file, Transition). The objection "Managers cannot dispatch themselves, so the chief of staff remains the single executor" is **open** (Objections row 2).
- **First measurement (the same day):** "In 48 hours the chief of staff chose about 99% of the specialists' work"; 223 logged dispatches, all `actor: chief-of-staff`; 0 dispatches carrying a `batch=` reference; 2 of 20 lanes had returned a manager batch; 95% of commits authored as `Claude`; and "the instruments that would show this… are dark or wrong" (`2026-10-16-retro-delegation.md` lines 7-17 and the "Headline" paragraph).
- **Cost seen afterwards:** the founder's throughput complaint ("you are working all the day but number of demos did not move") is answered by a diagnosis that manager rounds took 35% of the day's 18.65M tokens and new builds 8%, with new lessons falling from 852 (10-13 and 10-14) to 10 (10-15 and 10-16) (`company/decisions/2026-10-16-founder-throughput-for-10k.md`, Diagnosis). That record is open and its numbers are the chief of staff's and principal-engineer-ops' (c5a73a4), not independently checked by me.
- **Category:** designed (the rule); observed, with a re-checkable record (the retro's counts can be recomputed from `git log` and `company/ops/events.jsonl`; I did not recompute them).
- **Supports:** scalable oversight was attempted as an org rule; the company measured its own compliance and found the hub still in place; more process measurably cost throughput.
- **Does not support:** that the rule works; that coordination overhead is inherent rather than a first-week artefact.

### C7. The honest limits (VP candidate 7): ESTABLISHED, AND THE COMPANY WRITES THEM ITSELF
- **No real learners:** 0 of 1,283 lessons has `evidence.humanLearners` (python count over `src/demos/*/*/meta.json`); EXP-002 is "designed, not run" and board W-007 "Recruit 5 learners for EXP-002" (owner founder) is `backlog`. The latest handoff: "Everything rests on simulated walks and Chromium; nothing shows anyone learned." (progress.md line 14).
- **One model:** the company said it to the founder: "'Generate a company' is a strong claim; the evidence so far is one company with one model in many roles, no real learners, and the coordinator as hub." (`company/decisions/2026-10-16-founder-system3-meta-sibling.md`, Objections row 2, status open). The retro adds that "the model is the same; the written refusals are what make them differ" (`2026-10-16-retro-delegation.md`, What went well 4).
- **Coordinator as hub:** C6.
- **Category:** argued (the limits), resting on observed counts.

### C8. The release log runs ahead of production (my find)
- **What the external records show.** Vercel's commit statuses (GitHub API, read 2026-10-17) for the five commits logged as releases r1-r5 on 2026-10-14: `f868127` (r1) "Canceled by Ignored Build Step"; `6b45ea0` (r2) "failure (Deployment rate limited)"; `91274b8` (r3) and `f4537d7` (r4) "Canceled by Ignored Build Step"; `5e8608d` (r5) "Deployment has completed" (`deploy-marker/vercel-statuses-2026-10-17.txt`). r8's commit `6cbce514` is "failure (Deployment rate limited — retry in 24 hours.)" at 19:11:29Z. The Deploy-to-Vercel workflow ran five times for the r9 tree and its follow-ups on 2026-10-17, all `failure` at the step "Verify, build, deploy and smoke-test"; a sixth was `in_progress` at 14:44:59Z (`gh api …/actions/workflows/deploy.yml/runs`, then `/runs/<id>/jobs`).
- **What production served at 15:07Z on 2026-10-17** (`curl` of `https://system-3-company.vercel.app`): `/` 200 with header `age: 178975` (about 49.7 hours, i.e. built around 13:24Z on 10-15, after r7); `/d/heat-the-ammonia-maker` (published in r7) 200; `/d/snap-the-magnet`, `/d/where-the-axis-starts`, `/d/raters-reward-agreement` (published in r8, per releases.json) 404; `/d/left-or-right` (published in r9) 404.
- **What the release log says.** r2-r4 are entered as production releases; their own `known_issues` say "Whether Vercel built this commit is not recorded" (r2) and "this [deploy] commit was skipped by Vercel" (r4). r8 is entered with "live status not re-confirmed (Vercel API access denied to this session)". r9's summary says "deployed by the Deploy to Vercel workflow" (`company/ops/releases.json`).
- **Against a COE.** The deploy-bypass COE's Impact line says "Production received four content releases (`6b45ea0` 13:01, `91274b8` 13:51, `f4537d7` 14:27, `5e8608d` 14:43)" (`2026-10-14-coe-deploy-bypass-and-quota.md` line 23). By Vercel's statuses only `5e8608d` deployed; it carried the earlier content, so the COE's substantive point (lessons reached learners with no CI or QA verdict) stands, but its count of production releases does not.
- **Category:** observed, with a re-checkable record. The records are third-party (Vercel, GitHub Actions, the live site), the closest thing to an outside witness in this study. **For the fact-checker:** a deploy by another path (Vercel CLI) would not show as a commit status; I found no record of one. The 14:44Z run may since have succeeded. Production state is a moving target: recheck with the same commands and timestamp the answer.
- **Supports:** "the summary is not the record" at the company's own release layer; the release manager's honest flags ("not re-confirmed") were the correct posture; a third-party record decided what the agents' records could not.
- **Does not support:** any claim that the company concealed anything (the uncertainties are flagged in the entries); any claim about learners.
- **This contradicts statements in the company's records, and I report it as such; I do not edit them.** Route: release-manager and evaluation-steward (System 3 Company), through the head of book.

### C9. Founder override: "Ship it anyway" (r9, 2026-10-17)
- **What happened.** A launch-review ruling made a WebKit/Safari check a deploy-time precondition for `math/left-or-right`; the container could not run WebKit. The founder was shown the consequence ("If the card fails there, iPhone users see the mirror-image knot after 'Turn over'") and chose **"Ship it anyway"**. The record states the risk, what would make the decision wrong, the revert path, and that the waiver "is not a verification and is not carried to any later deploy" (`company/decisions/2026-10-17-founder-deploy-r9-left-or-right-safari.md`, lines 11-30).
- **Category:** observed, with a re-checkable record (the founder's words are quoted).
- **Supports:** Article 4.1's override procedure in use: a human waived a gate in writing, with the objection and its consequence kept (the Interlude's "objections keep their consequences"; Chapter 8's human in the loop that changes the loops).
- **Does not support:** that the risk was small (unverified), or that the deploy happened (see C8: at 15:07Z left-or-right was 404 in production).

### C10. `/dev/null` replaced on the shared host (COE 2026-10-16)
- **What happened.** A QA run executed `ln -sfn $QA_OUT /dev/null` as root; every agent's git and shell broke for about 2 min 25 s; the chief of staff restored the device; the run, unaware, repaired it a second time. The COE reads the run's own tool-call transcript as the record and the run's report as testimony, and notes "the two agree" (`company/rituals/records/2026-10-16-coe-dev-null-replaced.md`, provenance and timeline). It also records that "the classifier passed the destructive command (no sandbox flag) and refused the repair (sandbox flag)" (Impact, Gates).
- **Category:** observed, with a re-checkable record at the time (the transcript path it cites no longer exists on the host; the COE is the surviving record).
- **Supports:** shared mutable state with no owner is where narrow agents collide; the COE separated record from testimony explicitly.
- **Does not support:** anything about the model's competence in general.

### C11. `rebase --autostash` swept other agents' work (COE 2026-10-16)
- **What happened.** A push step written into manager briefs (`git rebase -q --autostash`) stashed every tracked change in the shared checkout and failed its clean-tree check because another agent wrote a file in between, leaving the stash orphaned and blocking all pushes; it happened at 10:50Z (undeclared) and again at 13:06Z. The author reproduced the mechanism in a scratch repo on git 2.43.0 and found a proposed `pre-rebase` hook "never runs on this path" (`company/rituals/records/2026-10-16-coe-shared-checkout-autostash.md`, practice, occurrences, mechanism).
- **Role caught in its own incident:** the author discloses that "the 10:50Z autostash 13e83c8 was made by a principal-engineer run", i.e. its own role, and keeps authorship with that disclosure (provenance line).
- **Category:** observed; the mechanism was **run** by the company in a scratch repo (not committed, so not rerunnable from the company's files).
- **Supports:** an instruction in a brief (prose) propagated a destructive practice across runs; the COE reproduced the mechanism instead of blaming a run.
- **Does not support:** that the guard now in place works under load (approved with conditions on 10-17, `company/engineering/readiness/2026-10-17-git-guard-git247-autostash.md`).

### C12. The QA label was a constant (audit 2026-10-16)
- **What happened.** `cmdQaRecord` writes "recorded by: qa-tester (company qa-record)" whoever runs it (`tools/company.mjs` line 631). Over 48 hours, 14 commits touched QA records: 2 traceable to a qa-tester dispatch, 7 to integration runs (the chief of staff, merges, builders, a contributor), 5 unknown; "197 of those 217" lessons listed "Ready to publish" rested on a QA record that was not independent; "Git names the qa-tester on none of them" (`company/reviews/org/2026-10-16-qa-record-authorship-audit.md`, totals and findings F1-F2).
- **Category:** observed, with a re-checkable record (the audit gives its `git log` commands).
- **Supports:** a gate can count evidence without being able to see who made it; the steward audited the gate's inputs and proposed an amendment (AMD-010 part 3) rather than editing the protected gate.
- **Does not support:** that any published lesson is broken.

### C13. Founder pressure and capacity: the host-exhaustion COE (2026-10-14)
- **What happened.** Up to 20 agents (18 builders) ran on a 4-CPU host; load 25-60; disk full several times; dev pages took up to 12 minutes; official QA could not run until about 18:00 (`company/rituals/records/2026-10-14-coe-host-exhaustion.md`, timeline). The COE records the founder's asks, "Spin 20 agents" (06:38), "We are under utilizing" (06:49, 12:26), "Spin many agents" (14:58), each "followed by a dispatch wave with no capacity answer" (same file; also operating audit F2, where the founder's spelling "Spin 20 agnets" is preserved). Root cause: "The host was a shared resource with no owner and no allocator." It also corrects an ops review that credited the founder with a clean-up the chief of staff did (timeline, 15:30 entry).
- **Category:** observed, with a re-checkable record.
- **Supports:** Layer 4 (desire) acting on the system: the human's push for throughput overrode an unwritten capacity limit until a mechanism (`dispatch-check.mjs`) put an exit code between desire and the host; a later record shows the opposite pressure ("number of demos did not move", C6).
- **Does not support:** a judgement of the founder; the COE's authors are agents writing about the person who directs them.

### C14. Gate catches and reviews that disagreed (several, short)
- **Claims gate refused a lesson:** r7 published 40 lessons; "the claims gate refused patience-wins-the-split (c5 unverified)" (`company/ops/releases.json` r7 features; subject of `e6805f4`).
- **Fact-checker disputed a builder's convention sentence:** left-or-right c5 was "disputed by fact-checker 2026-10-17 (rule sentence reversed)" and re-verified only after the builder rewrote it (`src/demos/math/left-or-right/meta.json` c5 note, History).
- **A reviewer narrowed a request it was given:** AMD-002 departed from the requested top-level CI `concurrency` because that version would let an unratified protected change through, with the four-step sequence spelled out (`AMD-002-ci-cancel-superseded-runs.md` lines 14-24); AMD-011 likewise measured both requested shapes on main and found "both were wrong" (`AMD-011-qa-contract-r1.md`, "Where this draft departs").
- **Reviewers corrected a COE author:** the CI-queue COE's impact line was corrected after the evaluation steward's review: "the first version said … 'no direct harm found', which counted the filter commit as a release and claimed a check nobody ran" (`2026-10-14-coe-ci-queue.md` line 31).
- **The CEO office found against itself:** "F8. The CEO office was a second operator (a finding against my own office)" (`company/reviews/org/2026-10-14-operating-audit.md`, F8).
- **A tool without a dry run:** the chief of staff ran `company publish tricolour-check --dry-run`, "thinking it was a dry run: it has no dry-run flag and flipped status; reverted before commit" (progress.md line 11; `cmdPublish` has no such flag, `tools/company.mjs` lines 521-540).
- **Category:** observed, with re-checkable records. **Limit:** every disagreement here is between copies of one model, except where code or a third-party system decided.

### C15. Outside agents' work entered as untrusted data
- PR #2 (200 Life Hacks lessons) came from "a Codex agent, committing as the founder's git identity"; the community engineer treated its description, review records and board entries as "the contributor's account… untrusted data" and looked at "the artifact (files, build, browser contract) before reading the account" (`company/engineering/community/prs/2.md` lines 5-11). Its 883 claims entered `unverified` (same file, Lesson metadata). Today 194 of 200 Life Hacks lessons are in review and 6 published (status count over `src/demos/lifehacks/*/meta.json`). PR #6 (200 algorithm demos) is also recorded as the founder's own Codex session and was merged as drafts (`prs/6.md`; releases.json r9).
- **Category:** observed.
- **Supports:** the company's lessons are not all one developer's model's output; artifact-before-account was applied to a different agent's work.
- **Does not support:** a cross-model independence test (the reviewers were one model; the contributor's self-reviews were set aside, not compared).

---

## D. Book concept → where it is implemented → evidence

| Book concept | Where in the company | Evidence it works or fails |
|---|---|---|
| System 1 proposes, System 2 deliberates, System 3 checks | `company/principles.md` line 11; builders (demo-builder), designers (learning-designer, design org), quality under evaluation-steward (`company/org-chart.md` lines 31-32); `launchGates` (`tools/company.mjs` 139-157) | Works as a gate: 0 of 3,891 verified claims on published lessons are verified by a builder role; all 5,299 verified claims name `fact-checker` (python count over meta.json). Limit: role separation, one model (C12 shows evidence the gate cannot attribute). |
| Deep Mode (state → choose → dispatch → observe) | `company/ops/operating-loop.md` lines 5-9; chief-of-staff role (`roles.mjs` line 55) | Works as a loop; failure mode is the hub: ~99% of dispatch chosen by one role (C6); records dropped when busy ("no progress.md entry for about 20 h", retro H7). |
| Trust chains, claim addresses | `meta.json` claims with id/support/source/status/note (A4); learner-facing trust sheet (releases.json r7 features) | 10,284 claims: 5,299 verified, 4,921 unverified, 14 disputed, 50 withdrawn; published lessons hold only verified or withdrawn claims (count). Not tested against real readers. |
| Society of agents / many knowers | 99 roles, 20 lanes (POC map in the org-and-dispatch decision); independence rules (`company/reviews/README.md`) | Specialists caught errors (C1, C2, C5, C14); the society's independence is unmeasured (EXP-001 not run). |
| Copies of one model are one witness | `company/principles.md` line 16; EXP-001 (book's test adapted) | Designed, not run. The company's own pattern on it was demoted from `**` to `*` for lack of a result. |
| Pattern language | `company/knowledge/patterns/` (27), with `would_be_wrong_if` and `known_failure`; Pattern Review | 0 patterns at `**`, 4 at `*`; many written from one day's COEs (e.g. "a-rule-without-a-mechanism-is-a-wish": "Four cases, all one day"). Accumulation is real; validation is not. |
| Recursive self-improvement; the judged do not amend the judge | Constitution Art. 3; protected paths, hook and CI; amendments AMD-000..012; COEs ending in mechanisms; org regenerated from data | Amendment process used (AMD-002, AMD-012 ratified; others proposed with departures argued); many COE actions remain open (C1); R&D "code evolution" with a fixed evaluator the candidates cannot edit (`company/rnd/evolution.md`, roles table). |
| Scalable oversight | Founder's dispatch-through-managers rule; dispatch-check exit codes; host-invariant spec; per-role memory | Designed; first measurement shows it not yet working (C6); overhead visible (throughput diagnosis). |
| Layer 4 (desire) | Founder owns Surface Value (protected) and the desire layer (`roles.mjs` line 26); founder intake rule (operating audit §2) | Founder pressure shaped capacity incidents (C13) and the 10k-lesson target (F-41); proposed Surface Value v2 adds an ad slot (AMD-008, proposed, not ratified), which the mission's "not in the attention business" will have to answer. |
| Fluent autonomy | Agents run end to end under gates; founder approves deploys and org changes | Not shown. Deploys still wait on the founder each time; the hub persists; no external outcome measured. The company's own records call its catches "checking the disk" (retro, What went well 2). |
| Evaluators see the artifact first | `company/reviews/README.md` rules 1, 6; walkthrough transcripts; PR #2 review (C15) | Followed in records (headings "written … before reading"); its effect on error survival is untested (EXP-001). |
| Objections travel with decisions | `check` lint (`tools/company.mjs` 289-290); constitution 4.2 | Records carry objections with statuses, many "open" with owners (e.g. org-and-dispatch rule row 2). "Carried forward" with no answer was found and flagged once (operating audit A5). |
| The disk is the memory | `CLAUDE.md` line 5; progress.md (269 entries); role memories (298 files); events.jsonl; releases.json | Works when read: several catches came from reading git, not reports (C1, C4). Fails when instruments go dark or stale: event log stopped ~25 h (retro H3); CLAUDE.md and README stale (A2, A8); the release log ahead of production (C8). |

---

## E. Numbers (each with the command)

All commands run in `/home/user/system-3-company` on 2026-10-17 unless noted.

| Number | Value | Command |
|---|---|---|
| Roles in the org data | 99 | `node -e "import('./tools/org/roles.mjs').then(m=>console.log(m.roles.length))"` |
| Agent definitions | 98 | `ls .claude/agents \| wc -l` |
| Role model settings | sonnet 48 · inherit 49 · unset 2 | node over `roles.mjs`, counting `model` |
| Lessons | 1,283 (published 720 · review 234 · draft 329) | python: `json.load` each `src/demos/*/*/meta.json`, count `status` |
| Domains with lessons | 14 | `ls src/demos` (directories) |
| Claims | 10,284 (verified 5,299 · unverified 4,921 · disputed 14 · withdrawn 50) | same python, over `claims[]` |
| Claim support types | derivation 7,021 · convention 1,480 · source 1,216 · simulation 567 | same |
| Claims on published lessons | 3,922 (verified 3,891 · withdrawn 31) | same, filtered `status == published` |
| Lessons with human-learner evidence | 0 | same, `evidence.humanLearners` non-empty |
| Decision records | 85 (33 with "founder" in the file name) | `ls company/decisions \| grep -c '^2026'`; `… \| grep -c '^2026.*founder'` |
| COEs | 7 | `find company -ipath '*coe*' -type f` minus the template |
| Ritual records | 68 | `ls company/rituals/records \| wc -l` |
| Amendment files | AMD-000, 001, 002, 005, 006, 008, 010, 011, 012; ratified: 000, 002, 012 | `ls company/constitution/amendments`; status lines |
| Patterns | 27 (0 at `**`, 4 at `*`) | `ls company/knowledge/patterns`; `grep -h '^confidence'` |
| Experiments | 8 numbered, 0 with a result | `ls company/experiments`; status lines |
| Board items | 1,667 (backlog 843 · done 559 · review 151 · next 54 · dropped 54 · doing 6) | python over `company/ops/board.json` `items[].state` |
| Handoff entries | 269 | `grep -c '^## ' company/ops/progress.md` |
| Commits on the default branch | 2,718 | `gh api -i "repos/hanialshater/system-3-company/commits?sha=ccr-4c6c7654-ew9ko1&per_page=1"` → Link `rel="last"` page |
| Commits visible in the local (shallow) clone | 1,666 | `git rev-list --all --count` |
| Commit authors (local clone) | `Claude` 1,532 of 1,666; founder identity 17 | `git log --all --format='%an' \| sort \| uniq -c` |
| Days of operation | 4 d 15.5 h (2026-10-12 22:51Z → 2026-10-17 14:21Z) | first and last commit via the API (pages 2718 and 1) |
| Releases logged | 9 (r1-r9); Vercel shows completed deploys for r5, r6, r7 commits; failures for r2 and r8 | `company/ops/releases.json`; `deploy-marker/vercel-statuses-2026-10-17.txt` |
| Measured subagent tokens | 113.1M over 992 runs (2026-10-12 23:04Z → 2026-10-16 15:27Z; coordinator excluded; known gaps) | python sum of `tokens` in `company/ops/ledger.jsonl` |
| Dispatch events logged | 1,174 (last 2026-10-16 19:04Z) | `grep -c '"type":"dispatch"' company/ops/events.jsonl` |
| Planted-bug new run | 15 of 15 caught, counts as reported | `node plant/plant.mjs <export> plant/result-2026-10-17.json` (this folder) |

---

## F. Honest limits, and questions only the founder can answer

**What the company has not shown**
- **Real learners:** none. 0 lessons carry human-learner evidence; EXP-002 is not run; the recruiting item is the founder's and in backlog (C7). No lesson is shown to teach.
- **External witnesses:** almost none. Apart from the founder, the only non-model witnesses are third-party system records and executed code. EXP-001 (the book's one-witness test, adapted) is not run.
- **Production, as of 15:07Z 2026-10-17:** the live site appears to serve a build from about r7 (C8). Most of the company's work since 10-15 has not reached anyone outside it.
- **Scale and time:** under five days, one host (4 CPUs), one coordinator; a 10,000-lesson ambition with a diagnosed throughput collapse (C6).
- **Cost:** 113.1M measured subagent tokens is a lower bound (coordinator and gaps excluded). No money figure exists in the records I read.
- **The shallow clone:** some commits cited by the company's records are not in my local history; I read the ones I needed through the API. A full clone would let the fact-checker recheck the rest.
- **Testimony layers:** many numbers in the company's records (lesson counts per day, the retro's dispatch shares, the throughput diagnosis) are agents' measurements I did not recompute.

**Questions for the founder (listed, not answered)**
1. May the book quote your words to the company (examples in G), including misspellings as typed, or should they be paraphrased?
2. May the book name the vendors (G), the repository and the live URL?
3. At Amazon or Zalando, did a deploy-marker class of incident happen (a literal token in prose firing a release), and what was fixed: the person or the mechanism?
4. Did those organisations have the coordinator-as-hub problem C6 measures, and what broke it?
5. How did the push for throughput ("spin many agents") compare with how you pushed teams at scale, and who told you no?
6. Is the company's role inflation (26 → 99 roles in five days) something you saw in human organisations?
7. Will you run EXP-002 (five real learners) before the chapter is accepted, so the chapter can report a real-learner result or say plainly that there is none?
8. Do you want the press to run the Note on Evidence's planted-diagnosis test (or EXP-001) inside the company, as a separate commission?
9. Which parts of the old store chapter's lived prototype must survive the rewrite?
10. Is the Codex contribution (C15) yours to describe, and how do you want the tool named?

---

## G. Material sensitivity

**The founder's words to the company that a draft might quote (each needs the founder's acceptance; quote exactly or not at all):**
- "yes, deploy r7" (`2026-10-15-coe.md` line 8)
- "Ship it anyway" (`2026-10-17-founder-deploy-r9-left-or-right-safari.md` line 12)
- "Ok but we cut the deploymenta until we get an approval" (`2026-10-16-founder-no-git-deployments.md` line 8)
- "Make sure you use our org structure. Ok lets add very important rule for you, you never start new agents directly…" and "your scope is too big so you need to have scalable oversight through others" (`2026-10-16-founder-org-and-dispatch-rule.md`)
- "Spin 20 agnets do the algorithms demos", "We are under utilizing FYI", "Spin many agents" (`company/reviews/org/2026-10-14-operating-audit.md` F2)
- "We need to make sure we have good structure and rituals, you cant go random across the company" (operating audit header)
- "What is going on you are working all the day but number of demos did not move", "We should achieve more TBH I smell a problem" (`2026-10-16-founder-throughput-for-10k.md`)
- "Ah i did not do prod just dev and preview" (`2026-10-15-founder-f01-accounts.md` line 37)
- "It is System 3; we call it science." and the System 3 Meta vision naming Lovable and Replit (`2026-10-16-founder-system3-meta-sibling.md`)

**Service and vendor names in the sources (generalise unless the founder accepts naming):** Vercel (hosting; free-plan limit of 100 deployments a day), GitHub and GitHub Actions, Neon (Postgres), Resend (email), Better Auth, Playwright, Next.js/React, Codex (the contributing agent), Lovable and Replit (in the founder's words), Claude/Anthropic model names (Opus, Sonnet) in commit trailers and role data; regions ("Frankfurt", `fra1`).

**Identifiers to keep out of the book:** the founder's email address (in git author lines), Claude session URLs (commit trailers), host paths and transcript paths (e.g. `/root/.claude/projects/...`), board item ids are harmless but meaningless to readers. The live production URL appears in records; whether to print it is the founder's call.

**Credentials:** none copied. The sources name environment variables (`VERCEL_TOKEN`, `RESEND_API_KEY`) but I saw no values, and this record holds none.

**Persona names:** agents have human first names (`tools/org/people.mjs`). A chapter that uses them should say they are agents' labels.

---

## Files in this folder

- `record.md`: this record.
- `deploy-marker/`: `replay.sh` (C1 replay), `vercel.json.at-aefb10a`, `messages/<sha>.txt` (commit messages fetched through the API), `replay-result-2026-10-17.txt`, `vercel-statuses-2026-10-17.txt` (C1, C8).
- `plant/`: `plant.mjs`, `README.md`, `result-2026-10-17.json` (C5).

## Handoff (experiment-developer-system-3, 2026-10-17)

- **Changed:** created this folder only. Nothing in System 3 Company was modified (read-only `git`, `gh api` GETs, file reads, `curl` GETs of the public site; the planted-bug run used a `git archive` export in my scratchpad and a scratch TypeScript install). Not committed.
- **Believe:** high confidence in sections A, B, E (each number has its command); high in C1, C5 (run), C8's third-party statuses; medium in C8's reading of the live site (a CLI deploy or the in-progress run could change it); C2's reviewer split and C4's link between report and commit are not established, and C3's attribution is contradicted by the company's own retro.
- **Next:** fact-checker-system-3 checks this record against the sources (the C8 contradiction first, with fresh timestamps); head-of-book-system-3 decides whether to commit `deploy-marker/` and `plant/` (they become reproducible "run" evidence only once committed) and routes C8 to System 3 Company's release-manager and evaluation-steward; the founder answers section F's questions and G's permissions before the writer quotes anything.
- **Blocked:** nothing for this record. Running the Note on Evidence test or EXP-001 needs a separate commission.

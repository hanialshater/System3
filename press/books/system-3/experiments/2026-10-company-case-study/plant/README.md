# Planted-bug harness (record item C5)

A new run, not a rerun. The company's two original harnesses (the builder's ten bugs and principal-engineer-ops' twelve) were scratch scripts and were never committed. The ops script's path, `/tmp/claude-0/-home-user/3e472d64-…/scratchpad/ops-plant/plant.mjs`, does not exist on the host on 2026-10-17. `plant.mjs` here was written from the bug descriptions in `company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md`.

## Reproduce

```sh
# 1. Export the company repo at the commit you want, outside the checkout (read-only for the repo)
mkdir -p /tmp/plant-base && git -C /home/user/system-3-company archive <commit> src/lib tests/lifehacks src/kit src/demos/lifehacks package.json tsconfig.json | tar -x -C /tmp/plant-base
# 2. TypeScript 5.9.2 (the version in package-lock.json), the test loader's only dependency
mkdir -p /tmp/tsdeps && (cd /tmp/tsdeps && echo '{}' > package.json && npm install typescript@5.9.2)
ln -s /tmp/tsdeps/node_modules /tmp/plant-base/node_modules
# 3. Run
node plant.mjs /tmp/plant-base result.json
```

## Run of 2026-10-17

- Commit: `e84b8784b89ea5e5126011c6e2ac366ce6319d7b` (HEAD of the company's default branch, 2026-10-17 14:21Z). The test file and the three engine files that are mutated (`studyRecall.ts`, `studyModels.ts`, `studyStages.ts`) have the same blob hashes as at `59489384f`, the commit of the readiness record's approval. `studyCatalog.ts` (data) differs.
- Node v22 (see `result-2026-10-17.json`), TypeScript 5.9.2.
- Result: baseline 42/42; **15 of 15 applied mutations caught, each with the failing-test count the readiness record printed**; 42/42 after restore.
- Not reproduced (no single unambiguous substitution from the prose, so not guessed): builder rows 7, 8 and 10 (`scheduleObservation` claimed sentence on an overlapping layout; `dueRowOf` slug list dropped; watched job indexed by id), ops rows 8, 9, 10 and 12 (only the first clash named; claimed-minutes sign flipped; `plural` zero as singular; dependency/switches wording swapped).

## What it supports and does not

- Supports: the committed test file `tests/lifehacks/study-engine.test.mjs` fails on 15 of the 22 described bugs, with the reported counts. The readiness record's description of those 15 is consistent with the code.
- Does not support: that the original 22-bug runs happened as described (they remain testimony), the 7 rows not reproduced, or anything about the tests' adequacy beyond these mutations. The mutations were chosen by the same model family that wrote the tests (one model in many roles).

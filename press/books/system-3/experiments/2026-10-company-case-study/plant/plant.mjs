#!/usr/bin/env node
// Planted-bug harness for System 3 Company's Life Hacks study engine (record item C5).
// A NEW run, written by experiment-developer-system-3 on 2026-10-17 from the bug descriptions in
// company/engineering/readiness/2026-10-15-lifehacks-study-tp3-tp4-tp5.md (the original scratch
// scripts were never committed and no longer exist on the host). It is not a rerun of those scripts.
//
// Usage: node plant.mjs <export-dir> [out.json]
//   <export-dir> is a `git archive` export of the company repo (src/lib, tests/lifehacks, package.json,
//   tsconfig.json) with node_modules/typescript available (5.9.2, as pinned in package-lock.json).
// It refuses to run inside the company's own checkout: it edits engine files (one at a time, restored after each).
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";

const dir = path.resolve(process.argv[2] || "");
const out = process.argv[3];
if (!process.argv[2] || dir.startsWith("/home/user/system-3-company")) {
  console.error("usage: node plant.mjs <scratch export dir> [out.json]  (never the company checkout)");
  process.exit(2);
}
const L = "src/lib/lifehacks/";
// Each mutation: id, whose list it reproduces (B = builder's ten, O = ops reviewer's twelve), the row it
// reproduces as described in the readiness record, the expected failing-test count printed there, and an
// exact text substitution. Rows whose prose could not be mapped to one unambiguous substitution are omitted
// (listed in the record), not guessed.
const M = [
  { id: "B1", row: "retrievalProblems: repeated-choice check removed", expected: 1, file: L + "studyRecall.ts",
    from: "      if (new Set(p.choices).size !== p.choices.length) out.push(`${p.cue}: repeated choice`);\n", to: "" },
  { id: "B2", row: "nextChoice: an empty box starts at the second choice", expected: 1, file: L + "studyRecall.ts",
    from: "return current < 0 ? 0 :", to: "return current < 0 ? 1 :" },
  { id: "B3", row: "scoreRow: an empty box no longer makes the row incomplete", expected: 2, file: L + "studyRecall.ts",
    from: " && picks.every((p) => p >= 0), misses", to: ", misses" },
  { id: "B4", row: "markAttempt: ignores the attempt and reads the first choice", expected: 2, file: L + "studyRecall.ts",
    from: "spec.choices[i][attempt[i]] === c", to: "spec.choices[i][0] === c" },
  { id: "B5", row: "scheduleLayout: chain adds the next row's duration, not the previous one's", expected: 3, file: L + "studyModels.ts",
    from: "rows[i].start = rows[i - 1].start + rows[i - 1].duration", to: "rows[i].start = rows[i - 1].start + rows[i].duration" },
  { id: "B6", row: "freeGaps: at = end instead of Math.max(at, end)", expected: 1, file: L + "studyModels.ts",
    from: "at = Math.max(at, end);", to: "at = end;" },
  { id: "B9", row: "queueObservation: goal sentence on equal waiting (>= for >)", expected: 1, file: L + "studyStages.ts",
    from: "v.waiting>base.waiting) text+=", to: "v.waiting>=base.waiting) text+=" },
  { id: "O1", row: "retrievalProblems: compound 'no miss' check removed", expected: 1, file: L + "studyRecall.ts",
    from: ' else if (r.parts.every((p) => p.given === p.answer)) out.push("the stipulated attempt has no miss");', to: "" },
  { id: "O2", row: "retrievalProblems: feedback check only asks that a choice list exists", expected: 1, file: L + "studyRecall.ts",
    from: "if (!r.choices[i]?.includes(c))", to: "if (!r.choices[i])" },
  { id: "O3", row: "scoreRow: complete ignores the pick count", expected: 1, file: L + "studyRecall.ts",
    from: "complete: picks.length === row.prompts.length && picks.every", to: "complete: picks.every" },
  { id: "O4", row: "nextChoice: clamps at the last choice instead of wrapping", expected: 1, file: L + "studyRecall.ts",
    from: "(current + 1) % choices.length", to: "Math.min(current + 1, choices.length - 1)" },
  { id: "O5", row: "freeGaps: skip ignored", expected: 4, file: L + "studyModels.ts",
    from: "rows.filter((_, i) => i !== skip)", to: "rows.filter(() => true)" },
  { id: "O6", row: "freeGaps: trailing gap before the window dropped", expected: 4, file: L + "studyModels.ts",
    from: "  if (at < window) gaps.push({ start: at, end: window });\n", to: "" },
  { id: "O7", row: "scheduleLayout: long overrun added to every row", expected: 2, file: L + "studyModels.ts",
    from: "(long && spec.longer?.row === i ?", to: "(long && spec.longer ?" },
  { id: "O11", row: "queueObservation: atTarget uses some instead of every", expected: 1, file: L + "studyStages.ts",
    from: "const atTarget=order.every(", to: "const atTarget=order.some(" },
];

function runTests() {
  const r = spawnSync(process.execPath, ["--import", "./tests/lifehacks/register.mjs", "--test", "tests/lifehacks/study-engine.test.mjs"],
    { cwd: dir, encoding: "utf8", timeout: 300000 });
  const n = (k) => Number((r.stdout.match(new RegExp(`^# ${k} (\\d+)`, "m")) || [])[1] ?? NaN);
  return { pass: n("pass"), fail: n("fail"), tests: n("tests") };
}

const results = { harness: "plant.mjs", ranAt: new Date().toISOString(), dir, node: process.version, baseline: runTests(), mutations: [] };
for (const m of M) {
  const p = path.join(dir, m.file);
  const orig = fs.readFileSync(p, "utf8");
  const hits = orig.split(m.from).length - 1;
  if (hits !== 1) { results.mutations.push({ ...m, applied: false, reason: `substitution matched ${hits} times` }); continue; }
  fs.writeFileSync(p, orig.replace(m.from, m.to));
  try { const t = runTests(); results.mutations.push({ id: m.id, row: m.row, file: m.file, expected: m.expected, applied: true, failing: t.fail, tests: t.tests, caught: t.fail > 0 }); }
  finally { fs.writeFileSync(p, orig); }
}
results.after = runTests();
const caught = results.mutations.filter((x) => x.caught).length, applied = results.mutations.filter((x) => x.applied).length;
results.summary = `${caught} of ${applied} applied mutations caught; baseline ${results.baseline.pass}/${results.baseline.tests}; after restore ${results.after.pass}/${results.after.tests}`;
console.log(JSON.stringify(results, null, 2));
if (out) fs.writeFileSync(out, JSON.stringify(results, null, 2) + "\n");

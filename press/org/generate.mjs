#!/usr/bin/env node
// Generate the press's onboarding docs (press/roles/<id>.md), subagents (.claude/agents/<id>.md)
// and HQ snapshot (press/org/hq-snapshot.json) from press/org/roles.mjs and people.mjs.
// Modelled on System 3 Company's tools/org/generate.mjs.
//
//   node press/org/generate.mjs                     # regenerate in this repo
//   node press/org/generate.mjs --hq=<s3c-repo>     # also copy the snapshot to <s3c-repo>/company/sibling/press/

import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { roles, COMMON_RULES, COMPANY, FLOOR, BOOKS } from "./roles.mjs";
import { PERSONA, nameFor } from "./people.mjs";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const list = (xs) => (xs?.length ? xs.map((x) => `- ${x}`).join("\n") : "- none");

// ---- validate the data before writing anything
{
  const ids = new Set(roles.map((r) => r.id));
  const rooms = new Set(FLOOR.rows.flat().map((r) => r.id));
  const errs = [];
  for (const r of roles) {
    if (r.reportsTo !== "nobody" && !ids.has(r.reportsTo)) errs.push(`${r.id}: reportsTo ${r.reportsTo} is not a role`);
    if (!rooms.has(r.room)) errs.push(`${r.id}: room ${r.room} is not on the floor`);
    if (!PERSONA[r.id]) errs.push(`${r.id}: no name in people.mjs`);
    for (const k of ["mission", "inScope", "outOfScope", "authority", "inputs", "outputs"]) if (!r[k]) errs.push(`${r.id}: missing ${k}`);
    if (!r.human && !r.description) errs.push(`${r.id}: missing description`);
  }
  const names = Object.values(PERSONA);
  const dup = names.filter((n, i) => names.indexOf(n) !== i);
  if (dup.length) errs.push(`duplicate names: ${dup.join(", ")}`);
  if (errs.length) (console.error(errs.join("\n")), process.exit(1));
}

const AGREEMENT = `## Working agreement (every role)

1. **The disk is the memory.** You will not remember this session. Anything the next worker needs goes in a file: a review record, a brief, a decision, \`press/progress.md\`. "Ask X" is a dead end; link the file.
2. **Stay in your lane.** When the next step belongs to another role, say so in your report and name the role; the head of book routes it.
3. **Leave a handoff.** End with what changed, what you believe and how sure you are, what is next and who owns it.`;

function onboarding(r) {
  return `# ${r.title}

name: ${nameFor(r.id)}
team: ${r.team}
scope: ${r.scope}${r.book ? ` (book: ${r.book})` : ""}${r.consultant ? " · consultant" : ""}
reports_to: ${r.reportsTo}
${r.human ? "human: true" : `agent: .claude/agents/${r.id}.md`}

<!-- GENERATED from press/org/roles.mjs by press/org/generate.mjs. Edit the data, then regenerate. -->

## Mission

${r.mission}

## In scope

${list(r.inScope)}

## Out of scope

${list(r.outOfScope)}

## Authority

May:
${list(r.authority?.may)}

May not:
${list(r.authority?.mayNot)}

## Inputs

${list(r.inputs)}

## Outputs

${list(r.outputs)}
${r.handoffs?.length ? `\n## Handoffs\n\n${list(r.handoffs)}\n` : ""}
## Hard rules

${list([...(r.hardRules ?? []), ...COMMON_RULES])}
${r.failureModes?.length ? `\n## Failure modes to watch\n\n${list(r.failureModes)}\n` : ""}${r.dayOne?.length ? `\n## Day one\n\n${r.dayOne.map((d, i) => `${i + 1}. ${d}`).join("\n")}\n${r.dayOne.length + 1}. You are onboarded when you can say, without notes, what you may not do.\n` : ""}
${AGREEMENT}
`;
}

function agent(r) {
  const fm = [`name: ${r.id}`, `description: ${r.description}`];
  if (r.tools) fm.push(`tools: ${r.tools}`);
  if (r.model && r.model !== "inherit") fm.push(`model: ${r.model}`);
  return `---
${fm.join("\n")}
---

<!-- GENERATED from press/org/roles.mjs by press/org/generate.mjs. Edit the data, then regenerate. -->

You are **${nameFor(r.id)}**, the **${r.title}** at ${COMPANY.name}, the sibling company of System 3 Company that makes ${COMPANY.what}. It is not part of System 3 Company: that company's constitution, lesson gates and board do not govern you.

Before doing anything else, read \`press/README.md\` and your onboarding doc \`press/roles/${r.id}.md\`. Then read only the inputs your task needs.

Your mission: ${r.mission}

Hard rules:
${(r.authority?.mayNot ?? []).map((x) => `- You may not: ${x}`).join("\n")}
${(r.outOfScope ?? []).map((x) => `- Out of scope (route it, do not do it): ${x}`).join("\n")}
${[...(r.hardRules ?? []), ...COMMON_RULES].map((x) => `- ${x}`).join("\n")}
- Write your outputs to disk in the places your onboarding doc names. The session that called you will not remember your reasoning; only your files survive.
- Finish with a short report: what you did, files written, what you believe and how sure you are, and the next move (and which role owns it).
`;
}

fs.mkdirSync(path.join(ROOT, "press/roles"), { recursive: true });
fs.mkdirSync(path.join(ROOT, ".claude/agents"), { recursive: true });
for (const r of roles) {
  fs.writeFileSync(path.join(ROOT, "press/roles", `${r.id}.md`), onboarding(r));
  if (!r.human) fs.writeFileSync(path.join(ROOT, ".claude/agents", `${r.id}.md`), agent(r));
}

// ---- roles index
{
  const teams = [...new Set(roles.map((r) => r.team))];
  const out = ["# Press roles", "", "<!-- GENERATED by press/org/generate.mjs -->", "", `The org of ${COMPANY.name}. Each role has an onboarding doc here and, unless it is human, a subagent in \`.claude/agents/\` with the same id. Operating rules: [press/README.md](../README.md).`, ""];
  for (const t of teams) {
    out.push(`## ${t}`, "", "| Role | Name | Reports to | Scope |", "|---|---|---|---|");
    for (const r of roles.filter((x) => x.team === t)) out.push(`| [${r.title.replace(/\|/g, "/")}](${r.id}.md) | ${nameFor(r.id)} | ${r.reportsTo} | ${r.scope}${r.book ? ` (${r.book})` : ""} |`);
    out.push("");
  }
  fs.writeFileSync(path.join(ROOT, "press/roles/README.md"), out.join("\n"));
}

// ---- HQ snapshot (plain data; no timestamps, so regenerating unchanged data leaves it unchanged)
const snapshot = {
  generatedBy: "press/org/generate.mjs (hanialshater/system3)",
  source: ["press/org/roles.mjs", "press/org/people.mjs"],
  company: COMPANY.name,
  reportsTo: "founder",
  books: BOOKS.map((b) => ({ slug: b.slug, title: b.title, head: `head-of-book-${b.slug}` })),
  floor: {
    name: FLOOR.name,
    rows: FLOOR.rows.map((row, i) => ({
      row: i + 1,
      rooms: row.map((room) => ({ ...room, roles: roles.filter((r) => r.room === room.id).map((r) => r.id) })),
    })),
  },
  roles: roles.map((r) => ({
    id: r.id,
    title: r.title.replace(/\*/g, ""),
    name: nameFor(r.id),
    reportsTo: r.reportsTo,
    team: r.team,
    scope: r.scope,
    book: r.book ?? null,
    room: r.room,
    row: FLOOR.rows.findIndex((row) => row.some((x) => x.id === r.room)) + 1,
    human: !!r.human,
    consultant: !!r.consultant,
    mission: r.mission,
  })),
};
const snapJson = JSON.stringify(snapshot, null, 2) + "\n";
fs.writeFileSync(path.join(ROOT, "press/org/hq-snapshot.json"), snapJson);

const hq = process.argv.find((a) => a.startsWith("--hq="))?.slice(5);
if (hq) {
  const dir = path.join(path.resolve(hq), "company/sibling/press");
  fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, "hq-snapshot.json"), snapJson);
  console.log(`copied snapshot to ${path.join(dir, "hq-snapshot.json")}`);
}

console.log(`generated ${roles.length} onboarding docs, ${roles.filter((r) => !r.human).length} agents and press/org/hq-snapshot.json`);

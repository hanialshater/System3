---
name: blind-bench
description: Blind, reproducible pairwise benchmarking of chapters or essays against comparator books (System 3 vs Sapiens, Human Compatible, Life 3.0, or versions of the same chapter) — Swiss tournament, full text, both orders, redacted names, recognition logging, judges from more than one vendor, Bradley–Terry scores with bootstrap intervals, per-criterion and per-book results, resumable JSONL cache. Use whenever the user asks to "benchmark", "run a tournament", "Bradley-Terry", "compare chapters blind", "rank my chapters against X", "is my book better than", or questions whether an earlier evaluation was biased, including when Claude itself knows which book is the author's.
---

# Blind bench

A score from a judge who knows which book is yours, read an excerpt, or saw the chapter in only one order is a claim, not a measurement. This skill exists because each of those happened once.

## What went wrong before (the reasons for every rule below)

- **Excerpt judging** punished chapters that build or turn in the middle (After Capacity; essay-shaped chapters of Human Compatible, Life 3.0 and Sapiens alike). Judge full text.
- **Reputation instead of reading.** Background knowledge of famous books is closer to their reputation than to a reading; it inflates famous chapters.
- **The judge knew the author** (memory, and an "Illustrated Reading Proof" author page). Say so whenever it's true.
- **Re-judging after pushback.** Two System 3 chapters were re-judged after the author objected, both moved up. Each change was defensible; the pattern is drift. Log every re-judgment with its trigger.
- **Self-preference.** A Claude judge may favour text about Claude or drafted with Claude. Only a judge from another vendor addresses that.
- **Rubric v1 flaws:** no level anchors; engagement and prose overlapped (double credit for narrative books); one bar for every chapter type (fiction lost on rigor); rigor as a quarter of every match.

## Workflow

1. **Build `chapters.json`.** Markdown: `scripts/md_chapters.py chapters S3 --order book-order.json --only-numbered`. PDFs: extract per chapter with the pdf-reading skill, check every chapter lands on the right text, and remove watermark or overlay layers (Human Compatible's PDF inserted fragments like "imDagination"). Don't ship extracted texts of published books; rebuild them locally from the user's PDFs.
2. **Choose the rubric** (`references/rubrics.md`). Default v2 reader-experience. State it in the results.
3. **Estimate cost first:** `bench.py --chapters chapters.json --estimate --rounds 6`. Full text is expensive (the 53-chapter run was ~312 calls and ~7.5M input tokens per judge). Start with two rounds.
4. **Smoke test:** `--dry-run` uses a deterministic mock judge.
5. **Run:** at least one non-Claude judge (`--judge openai:MODEL@BASE` covers OpenAI-compatible endpoints, including Gemini's). Both orders by default. Redact author names, book titles and self-references with `--strip`.
6. **Read the results:** overall Bradley–Terry with 95% bootstrap intervals, per-criterion fits, per-book means, and the recognition column (how often the judge named the right book). Overlapping intervals mean no ranking claim. Compare judges' rankings before pooling them.
7. **Report** with the caveats that still apply: which judges, whether they recognised the books, rubric version, chapters excluded, re-judgments and why.

## In-chat fallback

Without API keys, sub-agents or an artifact runner, a chat-only tournament is excerpt-limited and the judge is not blind. Either build the harness for the user to run, or a browser artifact that sends anonymous pairs to fresh sub-agents with sealed labels, randomised order and recognition questions, saving matches in the same JSONL format so results can be pooled later.

## Files

- `scripts/bench.py` — Swiss pairing, judges (anthropic, openai-compatible, mock), cache, BT fit, bootstrap, per-criterion and per-book tables, recognition counts.
- `scripts/md_chapters.py` — chapters.json from a Markdown chapter directory.
- `references/rubrics.md` — rubric v1 and v2 with anchors and known weaknesses.

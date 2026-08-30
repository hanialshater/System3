# Art Prompts — generation queue

One file per chapter; each job is a self-contained prompt for an external
image model. The return contract is the file path in each job's heading:
save the image there, commit, and the renderer picks it up by name on the
next `python3 book-design/render.py all`. See `../PIPELINE.md`.

Priority: chapter 8 and 13 openers (no asset exists), then the stale
renumbered openers (chapters 9, 10, 11 — chapter 12's is an open editorial
decision, ask before regenerating), then interior slots front to back.

- [Chapter 1 — Why I'm Betting on AI Agents](chapter-01.md): 5 jobs
- [Chapter 2 — The Algorithm Vortex](chapter-02.md): 2 jobs
- [Chapter 3 — The Vibe Coder's Seat](chapter-03.md): 5 jobs
- [Chapter 4 — System 3](chapter-04.md): 6 jobs
- [Chapter 5 — The Society of Agents](chapter-05.md): 5 jobs
- [Chapter 6 — Pattern Language](chapter-06.md): 5 jobs
- [Chapter 7 — Recursive Self-Improvement](chapter-07.md): 6 jobs
- [Chapter 8 — Scalable Oversight](chapter-08.md): 6 jobs
- [Chapter 9 — Layer 4](chapter-09.md): 6 jobs
- [Chapter 10 — Fluent Autonomy](chapter-10.md): 4 jobs
- [Chapter 11 — The Store That Builds Itself](chapter-11.md): 6 jobs
- [Chapter 12 — After Capacity](chapter-12.md): 6 jobs
- [Chapter 13 — The Prophecy](chapter-13.md): 5 jobs

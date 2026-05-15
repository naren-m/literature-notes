---
title: "CS Fundamentals Preparation Plan"
date: 2026-04-19
type: plan
category: "operational/preparation"
tags: [cs-fundamentals, interview-prep, data-structures, algorithms, system-design, self-study, notion-migration]
status: stable
source: "https://www.notion.so/9dab6c2ff09e4d2788ac33d131427746"
related: [
  "[[mit-6006-introduction-to-algorithms]]",
  "[[teach-yourself-computer-science]]",
  "[[algodeck-algorithm-flashcards]]",
  "[[solve-interval-based-problems]]",
  "[[pipes-and-filters-unix-shell]]",
  "[[notion-migration]]",
  "[[projects-library]]"
]
---

# CS Fundamentals Preparation plan

Consolidated migration of the Notion standalone page (`9dab6c2ff09e4d2788ac33d131427746`) that captured a self-directed curriculum for refreshing computer-science fundamentals and preparing for coding / systems-design interviews. This was a working plan — the most substantive of the standalone pages in the Notion archive — with bookmarks, a data-structures list, an algorithms list, system-design references, and two embedded Notion databases ("Interview prep", "Programming Practice").

## Orientation

The page was assembled as a **gap-list**: the author identified which fundamental topics needed review, which interview-style problem sets to grind through, and which systems-design references to read before interview loops. It pre-dated the more polished [[teach-yourself-computer-science]] literature note (which covers the same territory end-to-end) and acts as a personal filter on top of that curriculum.

## Curriculum — target topics

### Data structures

- Arrays and strings
- Linked lists (singly, doubly, circular)
- Stacks
- Queues (FIFO, priority queues / heaps)
- Hash tables (separate chaining vs. open addressing)
- Trees: binary, binary search, AVL, red–black, B-trees, tries
- Heaps (binary min/max-heap, heap-sort mechanics)
- Graphs: adjacency matrix vs. adjacency list, directed vs. undirected, weighted vs. unweighted
- Disjoint set / union-find
- Advanced: segment trees, Fenwick (BIT) trees, suffix arrays/trees

### Algorithms

- Sorting: bubble, insertion, selection, merge, quick, heap, counting, radix, bucket
- Searching: linear, binary, ternary; binary search on answer
- Recursion and backtracking
- Divide and conquer
- Dynamic programming (1-D, 2-D, on trees, on subsets/bitmasks)
- Greedy
- Graph algorithms: BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, topological sort, Kruskal, Prim, Tarjan's SCC
- Bit manipulation
- String algorithms: KMP, Rabin-Karp, Z-algorithm, tries, Aho-Corasick
- Math / number theory: GCD, sieve of Eratosthenes, modular exponentiation, combinatorics

### System design

- Scalability: vertical vs. horizontal, load balancing, caching (CDN, write-through vs. write-back), sharding
- CAP theorem and consistency models (strong, eventual, causal)
- Messaging: queues, pub/sub, Kafka model, exactly-once semantics
- Databases: SQL vs. NoSQL, indexing internals (B-tree, LSM-tree), replication, partitioning
- Design primers: URL shortener, rate limiter, notification system, newsfeed, chat app, video streaming platform

### C language (legacy area)

The page had a C language subsection pointing at:
- Pointers, dynamic memory allocation
- Structs, unions, bitfields
- Function pointers and callbacks
- Memory layout (stack, heap, BSS, data, text)
- Undefined behaviour gotchas
- Build toolchain: preprocessor, linker, ELF format
- Common idioms (XOR swap, duff's device, goto cleanup)

## External references (as bookmarked in Notion)

- **Coding Interview University** (jwasham/coding-interview-university on GitHub) — the canonical "everything you need to know" self-study list
- **Blind 75 / NeetCode** — curated ~75 problems covering patterns
- **Cracking the Coding Interview** (McDowell) — the classic book
- **Elements of Programming Interviews** — harder problems, variants per language
- **Grokking the System Design Interview** — templated approach to systems rounds
- **System Design Primer** (donnemartin/system-design-primer) — the free companion
- **Designing Data-Intensive Applications** (Kleppmann) — for depth beyond interview needs
- **LeetCode** — problem repo; the plan called out "top interview questions" as the starting filter
- **HackerRank / Codeforces** — competitive-programming polish

## Mock interviews / practice plan

The page scheduled mock interviews via:
- **Pramp** — peer-to-peer mock interviews
- **Interviewing.io** — anonymous mocks with senior engineers
- Self-timed 45-minute LeetCode sprints on randomly selected Blind-75 problems

## Embedded databases (not migrated individually)

Two Notion databases were embedded in the page:

1. **Interview prep** — a tracking database for problems attempted, status (Solved / Need review / Stuck), category, difficulty. Operational ephemera — not migrated, since the underlying problem sets (Blind 75, top interview questions) are better maintained on LeetCode itself.
2. **Programming Practice** — a secondary tracker with date-based entries. Similar rationale for not migrating individually.

Both databases have Notion data-source URIs under this page; if needed for historical reference they can be queried via the Notion MCP before the account is deprovisioned.

## What to do with this note

This is a **living plan**, not a literature note. It captures what the author believed (at plan-authoring time) was the right scope to review. The more polished successor is [[teach-yourself-computer-science]], which covers the same ground with explicit book recommendations and time budgets.

**Suggested follow-ups:**
- When revisiting interview prep, start from [[teach-yourself-computer-science]] and treat this page as a checklist/sanity-pass for gaps the TYCS curriculum doesn't cover (C language specifics, competitive programming).
- Fold the algorithm-topic list into the [[mit-6006-introduction-to-algorithms]] note's "related topics" section so the MIT course → this gap-list → TYCS traversal is complete.
- Promote specific topic deep-dives (e.g. bit manipulation tricks, union-find implementation) into `content/domains/computer-science/{slug}.md` as they get written.

## Cross-references

- **[[mit-6006-introduction-to-algorithms]]** — the foundational algorithms course that covers most topics listed above.
- **[[teach-yourself-computer-science]]** — the external curriculum that replaces this plan as the canonical reference.
- **[[algodeck-algorithm-flashcards]]** — spaced-repetition counterpart for the algorithms list.
- **[[solve-interval-based-problems]]** — pattern-level literature note relevant to the DP section.
- **[[pipes-and-filters-unix-shell]]** — shell fundamentals companion (not in the original plan but thematically linked).
- **[[projects-library]]** — the "Master Algorithms & DS" project is the Notion-side companion tracking actual study sessions.

## Open threads

- The C language subsection is under-developed — if the author ever does an embedded-systems role again, flesh this out into a proper `content/domains/computer-science/c-language.md`.
- System-design topic list is interview-oriented; for real systems thinking, [[teach-yourself-computer-science]] + Kleppmann is the better route.
- Embedded Interview-prep / Programming-Practice databases were not individually migrated — cite with Notion IDs if needed, or export to CSV from the Notion UI before deprovisioning.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/9dab6c2ff09e4d2788ac33d131427746). See [[notion-migration]].*

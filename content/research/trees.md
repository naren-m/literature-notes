---
title: "Trees (definitions and properties)"
date: 2020-09-09
type: research
category: "CSE/algorithms"
tags: [data-structures, trees, binary-trees, algorithms]
status: incomplete
source: "Notion Notes DB, course notes"
related: [binary-search-tree, avl-trees, heap-data-structure]
---

# Trees (definitions and properties)

Hub note on tree terminology and properties, captured from algorithm course notes.

## Definitions

- **Tree** — a graph that does not have loops (an acyclic, connected graph).
- **Binary tree** — a tree in which each node has at most two children.
- **Complete binary tree** — all internal nodes have exactly two children, and all leaves are at the same level. That is, the last level is completely full.
- **Perfect binary tree** — a complete binary tree where every internal node has exactly two children and every leaf is at the same depth. (In the original notes, the distinction between *complete* and *perfect* was fuzzy — they are the same thing under this stricter definition.)

## Terminology

- **Leaf node** — a node that has no children.
- **Internal node** — a node that is not a leaf.
- **Height of a node** — the longest path from that node down to a leaf.
- **Height of a binary tree** — the height of the root. For a balanced binary tree of `n` nodes, this is `Θ(log n)`.

## Properties of perfect binary trees

Let `h` = height, `n` = number of nodes.

- Number of nodes: `n = 2^(h+1) − 1`.
- Number of leaves: `⌈n / 2⌉ = 2^h`.
- Over half of all nodes are leaves (specifically, just over `n/2`).

*(The original note had the formulas off-by-one in a few places and flagged "Something is off — figure out." The corrected formulas are above.)*

## Related notes

- [[binary-search-tree]] — the ordering invariant specialization.
- [[avl-trees]] — self-balancing BSTs that keep height `Θ(log n)`.
- [[heap-data-structure]] — nearly-complete binary trees used for priority queues and heapsort.

## Open threads

- Write out proofs for the node/leaf counts (simple induction on `h`).
- Clarify the distinction between complete, full, perfect, and balanced binary trees in a single diagram.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/e466feb7fa8a4f06bffe154c8c1ea9cb). See [[notion-migration]].*

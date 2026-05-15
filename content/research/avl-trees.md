---
title: "AVL Trees"
date: 2020-10-12
type: research
category: "CSE/algorithms"
tags: [algorithms, data-structures, avl, balanced-bst, trees]
status: incomplete
source: "Notion Notes DB, course notes"
related: [binary-search-tree, trees]
---

# AVL Trees

Short stub on AVL trees, a self-balancing variant of the [[binary-search-tree]].

## Idea

AVL trees keep a BST close to fully populated at every height `h`, so the tree's height stays close to `log n` and all operations remain `O(log n)`.

The balancing invariant: for every node, the heights of its two subtrees differ by at most `1`.

## Operations

Standard BST operations, plus a rebalancing step:

- Insert, Delete.
- Min, Max.
- Successor, Predecessor.

## Rotations

Two primitive rebalancing operations:

- **Left rotate** — pivots the right child up.
- **Right rotate** — pivots the left child up.

Compound rotations (left-right, right-left) handle the zig-zag cases.

## AVL insert (sketch)

1. Insert as in a plain BST.
2. Walk back up to the root, and at each ancestor:
   - If the balance factor `|height(left) − height(right)|` becomes `> 1`, rotate to restore the invariant.

## Open threads

- Write out the four rotation cases (LL, RR, LR, RL) with diagrams.
- Explain the height bound `h ≤ 1.44 · log₂(n + 2) − 0.328…` that makes AVL trees strictly height-balanced.
- Compare with red-black trees (looser invariant, faster updates in practice).

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/5683ff4f1b5948fb9e5be5d45486e45f). See [[notion-migration]].*

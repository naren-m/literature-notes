---
title: "Binary Search Tree"
date: 2020-10-11
type: research
category: "CSE/algorithms"
tags: [algorithms, data-structures, bst, trees]
status: incomplete
source: "Notion Notes DB, course notes"
related: [trees, avl-trees]
---

# Binary Search Tree

Research stub on the BST data structure. The Notion original is mostly a structural outline; this note preserves the outline and flags the operations that still need to be written out.

## Definition

A **binary search tree (BST)** is a binary tree where:

1. Each node has at most two children.
2. For every node: the left subtree contains only keys less than the node's key, and the right subtree contains only keys greater than the node's key.

## Properties

- **Height of a BST**: `O(n)` in the worst case (degenerate into a linked list) and `O(log n)` when balanced. See [[avl-trees]] for a self-balancing variant that keeps height `Θ(log n)`.

## Operations

The following operations are placeholders in the original — fill in pseudocode and complexity analysis when promoting:

- **Insert** — walk down, attach new leaf.
- **Delete** — three cases (leaf, one child, two children — use in-order successor for the third).
- **Search** — walk down using the ordering invariant.
- **Traversal / Print**:
  - Pre-order: root → left → right.
  - In-order: left → root → right (yields sorted order for a BST).
  - Post-order: left → right → root.

## Open threads

- Flesh out each operation with pseudocode and complexity.
- Explain why in-order traversal produces sorted output, and link that to why BSTs are "search" trees.
- Link to [[avl-trees]] once balanced-tree operations are written.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/99afcda3d01c4f08a399c580cdb43cb3). See [[notion-migration]].*

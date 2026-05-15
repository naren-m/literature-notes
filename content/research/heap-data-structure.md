---
title: "Heap (data structure)"
date: 2020-09-09
type: research
category: "CSE/algorithms"
tags: [algorithms, data-structures, heap, priority-queue]
status: incomplete
source: "Notion Notes DB, course notes (Cormen-style algorithm course)"
related: [heapsort, trees, binary-search-tree]
---

# Heap (data structure)

Research note on the Heap data structure, captured from course notes. Exploratory — many operation sections are placeholders in the original.

## Definition

A heap can be viewed as a **nearly complete binary tree** that satisfies the *heap property*.

## Heap property

- **Min-heap property** — parent nodes are smaller than their children; the root is the smallest.
- **Max-heap property** — parent nodes are bigger than their children; the root is the largest.

## Kinds of heaps

- **Max-heap** — root is the largest element. Used in [[heapsort]].
- **Min-heap** — root is the smallest element. Used in priority queues.

## Used in algorithms like

- Priority queues.
- [[heapsort]].
- Dijkstra's algorithm (shortest path).

## Height of a heap

- For a heap of `n` elements, height is `Θ(lg n)`, because a heap is based on a complete binary tree.
- At height `h`: at most `2^(h+1) − 1` elements, at least `2^h` elements.

## Heap operations (to flesh out)

- Heapify (bubble down to restore heap property).
- Build-Heap (construct heap from array).
- Insert into heap.
- Delete from heap.
- Peek (read root without removing).
- Extract-Max / Extract-Min.
- Parent / Left / Right index arithmetic.

Each of these deserves a permanent note of its own once written in the user's own words.

## Open threads

- Fill in time complexities and pseudocode for each operation above.
- Add worked example of Build-Heap being `O(n)` rather than `O(n log n)` — this is a common source of confusion and is a good candidate for a permanent note.
- Connect to [[heapsort]] and to Dijkstra's algorithm.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/1d34aa4b3ffb4fb7ae66eb5c3672d3b1). See [[notion-migration]].*

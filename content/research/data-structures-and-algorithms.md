---
title: "Data Structures & Algorithms (hub)"
date: 2021-09-01
type: research
category: "CSE/algorithms"
tags: [data-structures, algorithms, hub, index]
status: incomplete
source: "Notion Knowledge DB — empty placeholder page linked to Algodeck resource"
related: [algodeck-algorithm-flashcards, sorting, trees, divide-and-conquer, recursion, asymptotic-notations]
---

# Data Structures & Algorithms (hub)

Top-level hub note for data structures and algorithms study. The Notion page was a blank placeholder that linked to the Algodeck flashcards resource. This note collects the subtopic notes that already exist in the vault and sketches the map of what should exist.

## What already exists in the vault

### Sorting

- [[sorting]] — hub note on sorting algorithms.
- [[merge-sort]], [[quick-sort]], [[insertion-sort]], [[heapsort]], [[counting-sort]], [[radix-sort]].

### Trees

- [[trees]] — definitions and properties of trees and binary trees.
- [[binary-search-tree]] — BST invariant, operations, complexity.
- [[avl-trees]] — self-balancing BST.
- [[heap-data-structure]] — nearly-complete binary tree used for priority queues and heapsort.

### Analysis

- [[asymptotic-notations]] — Θ, O, Ω, and their relationships.
- [[divide-and-conquer]] — the paradigm and how to solve recurrences (including the master theorem).
- [[recursion]] — base cases, recursive cases, and the induction analogy.

### Resources

- [[algodeck-algorithm-flashcards]] — Teiva Harsanyi's open-source flashcard deck for interview prep.

## What's missing (gaps to fill)

Core data structures not yet noted:

- Arrays, dynamic arrays (Python list, Java ArrayList, std::vector growth strategy).
- Linked lists (singly, doubly, circular).
- Stacks and queues, plus deques.
- Hash tables — the indispensable O(1) average-case lookup structure.
- Graphs — adjacency list vs. matrix, weighted vs. unweighted, directed vs. undirected.
- Tries and suffix trees.
- Disjoint-set / union-find.
- Segment trees and Fenwick (binary indexed) trees.

Core algorithm topics not yet noted:

- Graph search — BFS, DFS, topological sort.
- Shortest paths — Dijkstra, Bellman-Ford, Floyd-Warshall.
- Minimum spanning tree — Kruskal, Prim.
- Dynamic programming — memoization, bottom-up, classic problems (LIS, LCS, knapsack, edit distance).
- Greedy algorithms — when they work, when they don't.
- String algorithms — KMP, Rabin-Karp, Z-algorithm.
- NP-hardness — reductions, completeness, approximation.

## How to use this hub

When studying a new algorithm or data structure:

1. Add a new note under `content/research/` or `content/domains/algorithms/` named for the topic.
2. Update this hub's "What already exists" section with a wikilink.
3. Pull any reusable insights (like "Θ is the tight bound, O is the ceiling") into permanent notes under `content/domains/`.

## Related

- [[algodeck-algorithm-flashcards]] — the flashcard resource this hub originally bookmarked.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/ebab0d8fd69f43bd9c237af0ea200103). See [[notion-migration]].*

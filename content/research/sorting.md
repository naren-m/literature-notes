---
title: "Sorting (overview)"
date: 2020-09-09
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, lower-bounds, decision-trees]
status: incomplete
source: "Notion Notes DB, course notes"
related: [merge-sort, quick-sort, insertion-sort, counting-sort, radix-sort, heapsort]
---

# Sorting (overview)

Hub note for the sorting family of algorithms. Captures the comparison-based lower bound and links to individual algorithm notes.

## Individual sorting algorithms

- [[quick-sort]] — randomized partitioning, average `O(n log n)`.
- [[merge-sort]] — divide and conquer, `O(n log n)` worst-case.
- [[insertion-sort]] — simple, `O(n²)` worst-case.
- [[counting-sort]] — non-comparison, `O(n + k)` for keys in range `[0, k]`.
- [[radix-sort]] — non-comparison, repeated stable sort by digit.
- [[heapsort]] — uses the [[heap-data-structure]] to sort in `O(n log n)`.

## Why is the best comparison-sort complexity `n log n`?

Sorting finds the indices where sorted elements should live. Each comparison cuts the search space by about half (like binary search), giving `log n` depth, and each of the `n` elements is touched at least once — so `n · log n` is the lower bound for comparison sorts.

## Lower bound via decision trees

Any comparison sort can be viewed as a **decision tree** where:

- Each internal node is a binary comparison.
- Each leaf is an output (a specific permutation).
- One execution of the algorithm is a root-to-leaf path.
- The running time of the algorithm maps to the depth of the tree.
- The worst-case running time maps to the height of the tree.

### Lower-bound argument

- The tree must have at least `n!` leaves, because it must be able to output every possible permutation of `n` numbers.
- A binary tree with `n!` leaves has height `≥ log₂(n!) = Ω(n log n)`.
- Therefore any comparison sort has worst-case `Ω(n log n)` comparisons.

## Stable sort

A sort is **stable** if it preserves the relative order of equal elements. Merge sort and insertion sort are stable; quicksort and heapsort are not (without extra care).

## Open threads

- Write short permanent note: "Comparison sorts have `Ω(n log n)` lower bound because a binary decision tree must distinguish `n!` outputs." This is a clean, context-free fact worth distilling.
- Connect non-comparison sorts (counting, radix, bucket) to the lower-bound discussion — they beat `n log n` by not being comparison-based.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/c1d5560d94494a63bbef04a2ce91b9f5). See [[notion-migration]].*

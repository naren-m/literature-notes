---
title: "Heapsort"
date: 2020-09-09
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, heapsort, heap]
status: incomplete
source: "Notion Notes DB, course notes"
related: [heap-data-structure, sorting]
---

# Heapsort

Short research note on heapsort. Uses the max-heap property of the [[heap-data-structure]].

## Algorithm

1. **Build-Heap** — turn the input array into a max-heap in `O(n)` time.
2. Swap the root (max element) with the last element, then shrink the heap by one.
3. Call **Max-Heapify** on the new root to restore the heap property. Cost: `O(log n)`.
4. Repeat steps 2–3 until the heap size is `1`.

At termination, the array is sorted in ascending order.

## Complexity

- Time: `O(n log n)` (each of `n − 1` extractions costs `O(log n)`, dominating the initial `O(n)` build).
- Space: `O(1)` — in-place.
- Not stable: the swap step can reorder equal keys.

## Contrast with other `n log n` sorts

- **Merge sort** is stable but uses `O(n)` extra space.
- **Quick sort** is faster in practice (better cache behavior) but has `O(n²)` worst case without randomization.
- Heapsort's appeal: worst-case `O(n log n)` and in-place.

## Open threads

- Show why Build-Heap is `O(n)` (tight analysis via sum of heights).
- Write a worked example for a small array.
- Link to a future permanent note on "in-place vs stable trade-offs in sorting."

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/162d6ccdd9104732b2ef59feef9b007c). See [[notion-migration]].*

---
title: "Insertion Sort"
date: 2020-08-29
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, insertion-sort, loop-invariant]
status: incomplete
source: "Notion Notes DB, course notes"
related: [sorting, merge-sort, quick-sort]
---

# Insertion Sort

Research note on insertion sort. Captured as part of the MIT/Cormen sorting sequence — primarily a teaching sort used to illustrate correctness proofs via loop invariants.

## What is insertion sort?

Maintain a sorted prefix `A[1..j − 1]` and repeatedly take the next element `A[j]`, shift larger elements of the prefix one position right, and insert `A[j]` into its correct position. The prefix grows by one each iteration.

## When is it efficient?

- Best when sorting a **small** number of elements (small constants, good cache behavior).
- Real implementations (e.g., Timsort, libstdc++ introsort) fall back to insertion sort below some small threshold.

## Pseudocode (sketch)

```
Insertion-Sort(A):
    for j = 2 to length(A):
        key = A[j]
        i = j - 1
        while i > 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
```

## Is it in-place?

Yes — only `O(1)` extra storage.

## Loop invariant

*(The original Notion page synced a loop-invariant block that actually reflected the `Merge` routine of [[merge-sort]]. For insertion sort specifically the invariant is:)*

- **Initialization** — before the first iteration (`j = 2`), `A[1..j − 1] = A[1..1]` is trivially sorted.
- **Maintenance** — each iteration inserts `A[j]` into its correct place in the sorted prefix `A[1..j − 1]`, yielding a sorted `A[1..j]`.
- **Termination** — at `j = length(A) + 1`, `A[1..length(A)]` is the fully sorted array.

## Time complexity

- **Best case** (already sorted): `Θ(n)` — inner while loop exits immediately.
- **Worst case** (reverse sorted): `Θ(n²)` — every element shifts all the way back.
- **Average case**: `Θ(n²)`.

## Open threads

- Add the worked example `[5, 2, 4, 6, 1, 3]` step-by-step.
- Discuss stability (insertion sort is stable because the `A[i] > key` check is strict).
- Link to "why Timsort uses insertion sort for small runs" as a practical anchor.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/dc86ce034bf04be59650ff05b9448d16). See [[notion-migration]].*

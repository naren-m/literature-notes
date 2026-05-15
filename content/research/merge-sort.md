---
title: "Merge sort"
date: 2020-08-29
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, divide-and-conquer, merge-sort]
status: incomplete
source: "Notion Notes DB; CLRS; Programiz"
related: [sorting, insertion-sort, divide-and-conquer, recursion, asymptotic-notations, quick-sort, heapsort]
---

# Merge sort

> Divide-and-conquer comparison sort. Worst-case `Θ(n log n)`. Stable. The standard array implementation is *not* in-place.

## Overview

Merge sort follows the [[divide-and-conquer]] template:

1. **Divide** the array into two halves.
2. **Conquer** by recursively sorting each half.
3. **Combine** by merging the two sorted halves into a single sorted sequence.

The merge step is what makes the algorithm work — once both halves are sorted, merging them is linear in their combined length, which gives the `Θ(n log n)` total cost.

## Use cases for sorting (why we care)

- Finding the median.
- Binary search preconditions.
- Data compression.
- Computer graphics — for example, deciding which items should be rendered in a given order.

## Is merge sort in-place?

The standard array-based merge sort is **not in-place** — `MERGE` allocates auxiliary arrays `L` and `R` of size `Θ(n)`. The Notion source noted "Yes" here, which only holds for the linked-list variant of merge sort (where merging can be done by re-pointing nodes). See [Open threads](#open-threads).

## Algorithm pseudocode

CLRS-style pseudocode (chapter 2). Sentinels `∞` at the ends of `L` and `R` simplify the merge loop — it never needs to check whether one side has been exhausted.

```
MERGE-SORT(A, p, r)
  if p < r
    q = ⌊(p + r) / 2⌋
    MERGE-SORT(A, p, q)
    MERGE-SORT(A, q + 1, r)
    MERGE(A, p, q, r)

MERGE(A, p, q, r)
  n1 = q - p + 1
  n2 = r - q
  let L[1..n1+1] and R[1..n2+1] be new arrays
  for i = 1 to n1: L[i] = A[p + i - 1]
  for j = 1 to n2: R[j] = A[q + j]
  L[n1+1] = ∞
  R[n2+1] = ∞
  i = 1; j = 1
  for k = p to r
    if L[i] ≤ R[j]
      A[k] = L[i]
      i = i + 1
    else
      A[k] = R[j]
      j = j + 1
```

## Example

A small array gets recursively split down to singletons, then merged back up level by level. Each level does `Θ(n)` work across the merges at that level, and there are `Θ(log n)` levels — so total work is `Θ(n log n)`.

## Loop invariant for `MERGE`

Loop invariant for the inner `for k = p to r` loop:

> At the start of each iteration of the loop, the subarray `A[p..k-1]` contains the `k - p` smallest elements of `L[1..n1+1]` and `R[1..n2+1]` in sorted order. Moreover, `L[i]` and `R[j]` are the smallest elements of their arrays that have not been copied back into `A`.

### Initialization

Prior to the first iteration, `k = p`, so the subarray `A[p..k-1]` is empty. This empty subarray contains the `k - p = 0` smallest elements of `L` and `R`, and since `i = j = 1`, both `L[i]` and `R[j]` are the smallest elements of their arrays that have not been copied back into `A`.

### Maintenance

Suppose `L[i] ≤ R[j]`. Then `L[i]` is the smallest element not yet copied back into `A`. Because `A[p..k-1]` contains the `k - p` smallest elements, after copying `L[i]` into `A[k]` the subarray `A[p..k]` contains the `k - p + 1` smallest elements. Incrementing `k` (in the for-loop update) and `i` reestablishes the loop invariant for the next iteration. The case `L[i] > R[j]` is symmetric.

### Termination

At termination, `k = r + 1`. By the loop invariant, `A[p..k-1] = A[p..r]` contains the `k - p = r - p + 1` smallest elements of `L[1..n1+1]` and `R[1..n2+1]` in sorted order. The arrays `L` and `R` together contain `n1 + n2 + 2 = r - p + 3` elements; all but the two largest have been copied back into `A`, and those two are the sentinels.

## Time complexity

### `MERGE`

`Θ(n)` — each iteration of the merge loop does constant work and `k` ranges over `n = r - p + 1` positions.

### `MERGE-SORT`

`T(n) = 2·T(n/2) + Θ(n)` ⇒ `T(n) = Θ(n log n)`.

Breaking it down by the divide-and-conquer parts:

- **Divide.** Computing the midpoint is constant time, so `D(n) = Θ(1)`.
- **Conquer.** Recursively solve two subproblems of size `n/2`, contributing `2·T(n/2)`.
- **Combine.** `MERGE` on an `n`-element subarray runs in `Θ(n)`, so `C(n) = Θ(n)`.

The `Θ(n log n)` bound is the *worst case*, not just the average — there is no input ordering that makes merge sort faster than `Θ(n log n)`.

## Properties

- **Stable** — the `L[i] ≤ R[j]` (rather than `<`) tie-break preserves the original order of equal elements.
- **Not in-place** (array variant) — needs `Θ(n)` auxiliary memory for `L` and `R`.
- **Predictable** — same `Θ(n log n)` time on best, average, and worst case inputs, which makes it nice when worst-case latency matters.

## Open threads

- Reconcile the "in-place: yes" answer from the Notion source with CLRS — the standard array implementation is not in-place, but a linked-list merge sort can be. Pick one variant and state which.
- Compare to [[quick-sort]]: same `Θ(n log n)` average, but quick sort is in-place with smaller constants and better cache behavior, while merge sort wins on worst-case guarantees and stability.
- Add a note on **external merge sort** for sorting data that doesn't fit in memory — that's where merge sort really earns its keep.
- Candidate permanent note: "Merge sort's `n log n` comes from `n` work per level × `log n` levels of recursion."

## Related notes

- [[sorting]] — hub note for the sorting family and the `Ω(n log n)` lower bound.
- [[insertion-sort]] — the classic intro algorithm CLRS uses to teach loop invariants; merge sort's invariant follows the same template.
- [[divide-and-conquer]] — the general template merge sort instantiates.
- [[recursion]], [[asymptotic-notations]].

## References

- CLRS, *Introduction to Algorithms*, chapter 2 (Merge sort, loop invariants).
- Programiz, [Merge sort tutorial](https://www.programiz.com/dsa/merge-sort).

---

*Re-exported from Notion on 2026-05-09. Original: [Merge Sort](https://www.notion.so/ce4168d49acc41f08d1a1fbcf0060e09). Earlier abbreviated migration on 2026-04-19. See [[notion-migration]].*

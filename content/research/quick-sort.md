---
title: "Quick Sort and Randomized Algos"
date: 2020-09-07
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, quick-sort, randomized-algorithms, divide-and-conquer]
status: incomplete
source: "Notion Notes DB, course notes"
related: [sorting, merge-sort, insertion-sort, divide-and-conquer]
---

# Quick Sort and Randomized Algorithms

Research note on quicksort and why it pairs naturally with randomization.

## History

- Discovered by **C. A. R. Hoare** in 1962.

## Paradigm

- Divide and conquer (see [[divide-and-conquer]]).
- Benefits massively from randomizing the choice of pivot (or scrambling the input first).
- Essentially *recursive partitioning*.
- **In-place**: yes.

## Algorithm

- **Divide** — partition the array around a pivot `x` so that the lower subarray has elements `≤ x` and the upper subarray has elements `≥ x`.
- **Conquer** — recursively sort the two subarrays.
- **Combine** — trivial; nothing to do. The partition step already leaves the array in order.

## Time complexity

### Worst case

- Happens on already-sorted input with a naive pivot (e.g., always-first). Each partition degenerates so one side has `n − 1` elements and the other has `1`.
- Recurrence: `T(n) = T(n − 1) + T(1) + Θ(n) = T(n − 1) + Θ(n) = Θ(n²)`.
- Same asymptotic as [[insertion-sort]], which is interesting given how fast quicksort usually is.

### Best case

- Perfect split at the middle: `T(n) = 2 T(n/2) + Θ(n) = Θ(n log n)` by the master theorem.

### Unbalanced "lucky" case

- Even a skewed-but-constant split like `1/10 : 9/10` still gives `Θ(n log n)`:
  `T(n) = T(n/10) + T(9n/10) + Θ(n)`.
- Intuition: the recursion tree has depth `log₁₀/₉(n) = Θ(log n)` and each level does `O(n)` work.

### Lucky + unlucky alternation

- Alternating "good" and "bad" splits in the recurrence still yields `Θ(n log n)` expected time. This is the core of why randomized pivot selection gives expected `n log n` on **any** input.

## Why randomize the pivot?

Randomization breaks adversarial inputs: there is no fixed "bad" input because the algorithm itself introduces the randomness. Expected running time becomes `Θ(n log n)` regardless of input distribution.

## Open threads

- Write pseudocode for both Lomuto and Hoare partition schemes.
- Derive the expected `Θ(n log n)` via indicator random variables (Cormen §7.4).
- Compare constants with [[merge-sort]] — quicksort is usually ~2–3× faster in practice despite the same asymptotics.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/ed0884a24f5447d0beb3089c289d65ac). See [[notion-migration]].*

---
title: "Counting sort"
date: 2020-09-14
type: research
category: "CSE/algorithms"
tags: [algorithms, sorting, counting-sort, non-comparison-sort]
status: incomplete
source: "Notion Notes DB, course notes"
related: [sorting, radix-sort]
---

# Counting sort

Short research note on counting sort. Captured from algorithm course notes; needs to be fleshed out with pseudocode and complexity derivation.

## Idea

- Input: array `A[1..n]` where each `A[i] ∈ {0, 1, 2, …, k}`.
- Output: `B[1..n]` = sorted `A`.
- Auxiliary storage: an array of length `k + 1`.
- Assumption: keys are integers and each fits in a word.

Counting sort is **non-comparison-based**: it uses key values directly as indices into the auxiliary array, so it beats the `Ω(n log n)` lower bound for comparison sorts. See [[sorting]] for that lower bound.

## Sketch

1. Count occurrences of each key in `A`.
2. Turn counts into prefix sums — this gives, for each key `v`, the position where elements with key `v` should end in `B`.
3. Walk `A` in reverse and place each element into `B` at the right position, decrementing the prefix-sum counter as you go. Reverse order is what makes the sort **stable**.

## Complexity

- Time: `Θ(n + k)`.
- Space: `Θ(n + k)`.

Practical when `k = O(n)`; breaks down when the key range `k` is much larger than `n`.

## Open threads

- Write out the full pseudocode in the user's own voice.
- Add a worked example.
- Link to [[radix-sort]], which uses counting sort as its per-digit subroutine.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/fad526f3a26f414b8bdb7d7427cfad7f). See [[notion-migration]].*

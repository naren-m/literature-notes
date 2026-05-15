---
title: "Recursion"
date: 2020-08-09
type: research
category: "CSE/algorithms"
tags: [algorithms, recursion, programming, base-case]
status: incomplete
source: "Notion Knowledge DB stub (empty page)"
related: [divide-and-conquer, merge-sort, quick-sort]
---

# Recursion

Stub on recursion — a function calling itself on a smaller version of the same problem. The Notion page was a placeholder; this is the research note that would have grown there.

## The core idea

A function is **recursive** if it calls itself (directly or indirectly) on a smaller subproblem. Every recursive solution needs:

1. **Base case(s)** — one or more inputs small enough that the answer is immediate, no further recursion.
2. **Recursive case(s)** — a way to reduce the problem to one or more smaller instances of itself and combine their answers.
3. **Progress toward the base case** — each recursive call must strictly shrink the input in some well-founded sense, or the recursion won't terminate.

## Canonical examples

- **Factorial**: `n! = n · (n−1)!` with base case `0! = 1`.
- **Fibonacci**: `F(n) = F(n−1) + F(n−2)` with `F(0) = 0, F(1) = 1`. (Naive recursion is exponential — use memoization.)
- **Binary search** — halve the search range each call.
- **Tree traversals** — "visit root, recurse on each subtree."
- **Merge sort, quick sort** — classic divide-and-conquer recursive algorithms.
- **Tower of Hanoi** — the textbook "problem that's easy recursive, bewildering iterative."

## Recursion vs. iteration

- Every recursion can be converted to iteration (sometimes by simulating the call stack explicitly with a data-structure stack).
- **Tail recursion** — a recursive call that is the *last* thing the function does — can often be compiled into a loop (tail-call optimization). Scheme and some functional languages guarantee this; Python does not.
- Pick recursion when the problem **structure is recursive** (trees, nested data, divide-and-conquer) — the code will be shorter and clearer.
- Pick iteration when the problem is **flat and loop-shaped** — recursion would be overhead without clarity gain.

## Common pitfalls

- **Forgetting the base case** → infinite recursion → stack overflow.
- **Base case unreachable** because recursive progress doesn't actually shrink the problem in the dimension you think it does.
- **Exponential blow-up** from overlapping subproblems (naive Fibonacci). Fix with memoization / DP.
- **Deep recursion** hits the call-stack limit for large inputs. Convert to iteration or increase stack depth carefully.

## Proof by induction — recursion's logical twin

A recursive algorithm's correctness is typically proved by induction on the input size:

1. **Base case**: algorithm works for the smallest input.
2. **Inductive step**: if it works for all inputs strictly smaller than `n`, it works for `n`.

The structure of the induction proof mirrors the structure of the recursion.

## Candidate permanent notes

- **"Every recursion needs a base case that's reachable."** The single most common bug.
- **"Recursion = induction in executable form."** The conceptual bridge between math proofs and code.

## Related

- [[divide-and-conquer]] — a systematic way to structure recursive algorithms: divide, conquer, combine.
- [[merge-sort]], [[quick-sort]] — concrete recursive algorithms.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/11819799344c46d6bd7e70464643cbc9). See [[notion-migration]].*

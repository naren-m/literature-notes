---
title: "Divide and Conquer — Strassen, Fibonacci, Polynomial Multiplication"
date: 2020-09-06
type: research
category: "CSE/algorithms"
tags: [algorithms, divide-and-conquer, recurrences, master-theorem]
status: incomplete
source: "Notion Notes DB, course notes"
related: [merge-sort, quick-sort]
---

# Divide and Conquer — Strassen, Fibonacci, Polynomial Multiplication

Research hub on divide-and-conquer as a paradigm. Captured from course notes; many subsections are placeholders to flesh out later.

## Solving recurrences

The three standard techniques (each deserves its own permanent note once written out):

- **Substitution method** — guess the form of the solution, prove by induction.
- **Recursion-tree method** — draw the tree, sum the work per level, multiply by number of levels.
- **Master method** — `T(n) = a · T(n/b) + f(n)`; three cases determine whether the work is dominated by the leaves, the root, or is evenly distributed.

### Master theorem cases (reminder)

- **Case 1**: `f(n) = O(n^(log_b a − ε))` → `T(n) = Θ(n^log_b a)` (leaves dominate).
- **Case 2**: `f(n) = Θ(n^log_b a)` → `T(n) = Θ(n^log_b a · log n)` (work balanced across levels).
- **Case 3**: `f(n) = Ω(n^(log_b a + ε))` and regularity → `T(n) = Θ(f(n))` (root dominates).

### Intuition behind the master method

Compare `f(n)` (work at the root) to `n^log_b a` (work at the leaves). Whichever grows faster asymptotically wins; if they grow at the same rate, there's an extra `log n` factor.

## Divide and Conquer steps

- **Divide** — break the problem into one or more subproblems.
- **Conquer** — solve each subproblem recursively.
- **Combine** — stitch the subproblem solutions into a solution for the whole.

## Concrete D&C algorithms

Each of these can become its own permanent note:

- [[merge-sort]] — canonical `n log n` D&C sort.
- **Binary search** — `T(n) = T(n/2) + Θ(1) = Θ(log n)`.
- **Powering numbers** — `a^n` in `Θ(log n)` via repeated squaring.
- **Fibonacci numbers** — naive exponential; bottom-up `Θ(n)`; closed-form via golden ratio; recursive square-matrix algorithm in `Θ(log n)`.
- **Matrix multiplication** — standard `Θ(n³)`; naive D&C is also `Θ(n³)`; **Strassen's algorithm** achieves `Θ(n^log₂ 7) ≈ Θ(n^2.807)` via 7 recursive multiplications instead of 8.
- **VLSI layout** — not an algorithm per se but an application area where D&C shows up.

## Open threads

- Work out Strassen's 7-multiplication formula explicitly — it's the single most important concrete example of "clever D&C beats the obvious recurrence."
- Write a separate permanent note on the master theorem case 2 (the one that gives the extra `log n`).

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/442e52ad49274d9cb287084d493a3858). See [[notion-migration]].*

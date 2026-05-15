---
title: "Asymptotic Notations (Θ, O, Ω)"
date: 2020-08-24
type: research
category: "CSE/algorithms"
tags: [algorithms, asymptotic-analysis, big-o, complexity]
status: incomplete
source: "Notion Notes DB, course notes; supplemental YouTube lecture https://www.youtube.com/watch?v=EL9T1ngiCqA"
related: [sorting]
---

# Asymptotic Notations (Θ, O, Ω)

Research note on the three classical asymptotic notations used to describe algorithm running times.

## Formal definitions

Let `f` and `g` be non-negative functions on the positive integers.

- **Θ(g)** — `f ∈ Θ(g)` iff there exist constants `c₁, c₂, n₀ > 0` such that `c₁ · g(n) ≤ f(n) ≤ c₂ · g(n)` for all `n ≥ n₀`. This is a **tight** bound — both upper and lower.
- **O(g)** — `f ∈ O(g)` iff there exist `c₂, n₀ > 0` such that `f(n) ≤ c₂ · g(n)` for all `n ≥ n₀`. This is an **asymptotic upper bound**.
- **Ω(g)** — `f ∈ Ω(g)` iff there exist `c₁, n₀ > 0` such that `c₁ · g(n) ≤ f(n)` for all `n ≥ n₀`. This is an **asymptotic lower bound**.

Rule of thumb:

- Know both upper and lower → **Θ(n)**.
- Know only upper → **O(n)**.
- Know only lower → **Ω(n)**.

## Using asymptotic notation in practice

- Ignore constant multipliers.
- Focus on `n → ∞`.
- Consider only the leading term. Common growth rates, slowest to fastest: `log n < n < n log n < n² < n³ < 2ⁿ < n!`.

## Summary

1. Θ / O / Ω are used to express the time (or space) estimates of algorithms by:
   - Ignoring constant multipliers.
   - Taking `n → ∞`.
   - Keeping only the fastest-growing term.
2. Useful for reasoning about functions in general, not just algorithms.
3. `f(n) = o(g(n))` (little-o) means `f` is *asymptotically smaller* than `g`; similarly `ω` for strictly larger.

## Candidate permanent notes (not yet promoted)

- "Θ is the tight bound; O is the ceiling; Ω is the floor." This is the crispest one-line mnemonic in the material and would make a clean permanent note.
- "Little-o and little-omega are the strict versions." Same form, stronger inequality (`<` not `≤`).

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/8a7cc4ce05414cf4b553de2c648d87cb). See [[notion-migration]].*

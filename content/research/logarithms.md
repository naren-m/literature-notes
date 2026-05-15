---
title: "Logarithms"
date: 2020-08-16
type: research
category: "Math/algebra"
tags: [math, logarithms, exponents, algebra]
status: incomplete
source: "Notion Notes DB, course notes; referenced PDF 'Exponents and Logarithms'"
related: [number-theory-practicals, asymptotic-notations]
---

# Logarithms

Research note on logarithms — invented by **John Napier in 1614** to simplify multiplication and division by turning them into addition and subtraction.

## Three equivalent mental models

- `logₐ(x)` is the **number of times `x` must be divided by `a`** before reaching 1.
- `logₐ(x)` is the **number of times you must multiply `a` by itself to get `x`** (equivalently, the exponent in `a^? = x`).
- `logₐ(x)` is the **number of digits needed to represent `x` in base `a`** (up to a constant).

Canonical example: `log₂ 32 = 5` — because `2⁵ = 32`, or equivalently because `32 / 2 / 2 / 2 / 2 / 2 = 1` (five divisions).

## Relation to exponentials

The log and exponential are **inverse functions**:

- `a^(logₐ x) = x`
- `logₐ(a^x) = x`

So `log` "undoes" exponentiation and vice versa.

## Algorithmic relevance

- **Binary search** runs in `log₂ N` comparisons because each step halves the problem.
- **`Y`-ary search** runs in `log_Y N` steps — dividing a size-`Y` problem into `Y` subproblems repeatedly until a trivial (1-element) case.

## Properties

### Products, quotients, powers

- `log(m · n) = log(m) + log(n)` — **this is the whole reason logarithms exist**: they turn multiplication into addition.
- `log(m / n) = log(m) − log(n)`
- `log(1 / n) = −log(n)`
- `log(m^r) = r · log(m)`

### Change of base

- `logₐ(x) = log_b(x) / log_b(a)`
- `logₐ(x) = 1 / log_x(a)`
- `a^(log_b c) = c^(log_b a)` — a surprisingly useful identity for manipulating exponent towers.

### Special bases

- **Common log** — `log₁₀`, written plainly as `log` in engineering contexts.
- **Natural log** — `ln = logₑ`, where `e ≈ 2.71828…` is Euler's number, preferred in calculus because `d/dx(ln x) = 1/x`.
- **Binary log** — `log₂`, the default in computer science.

Note: the relative size of `log_a x` vs. `log_b x` differs only by a constant factor (`log_b x = log_a x / log_a b`), which is why big-O notation doesn't bother specifying a log base.

## Candidate permanent notes

- **"`log` turns multiplication into addition."** Napier's original motivation and the single most useful mental model.
- **"Log base doesn't matter in big-O."** Change-of-base is a constant factor, which O(·) absorbs.
- **"Binary search is `log₂ N` because each step halves the problem."** Connects the abstract log to a concrete algorithmic fact.

## Related

- [[number-theory-practicals]] — exponents and prime factorization share the multiplicative structure.
- [[asymptotic-notations]] — `log n` is the slowest-growing non-constant function you'll meet in complexity analysis.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/c64d464def104ed08ae949956e86b962). See [[notion-migration]].*

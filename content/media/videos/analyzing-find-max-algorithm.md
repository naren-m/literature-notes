---
title: "Analyzing Find-Max Algorithm (generating functions)"
date: 2020-08-24
type: literature
category: "CSE/algorithms"
tags: [algorithms, analysis-of-algorithms, generating-functions, video]
status: incomplete
source: "https://www.youtube.com/watch?v=sTFTCfrMWkk"
related: []
---

# Analyzing Find-Max Algorithm (generating functions)

Literature note from a YouTube lecture on algorithm analysis using generating functions. The running example is the trivial "find max of `x₁…xₙ`" algorithm and the question: on average, how many times does the running maximum variable get updated?

## What is "analysis of algorithms"?

A quantitative study of algorithms to measure how well they work. The term was coined by Donald Knuth. Correctness of a loop-based algorithm is typically argued with **loop invariants**, a technique introduced by Robert "Bob" Floyd.

## The four numbers to track

For a given quantity of interest (here, the number of times action `A` = "update `m`" happens):

- **Min** — best case. Here: `0` updates.
- **Max** — worst case. Here: `n − 1` updates.
- **Avg** — expected value over all inputs.
- **Dev** — standard deviation.

## Mean / expectation as a probability sum

For a variable `A` that takes values `0, 1, 2, …`:

```
Average = 0·P(A=0) + 1·P(A=1) + 2·P(A=2) + …
```

Enumerating probabilities directly for small `n` (e.g., `n = 3`) gives a pattern whose coefficients are known as **Stirling numbers**.

## Generating functions

A generating function is a (possibly infinite) polynomial whose coefficients are the terms of a sequence `aₙ`. Roughly: *generating functions transform problems about sequences into problems about functions.*

For the find-max analysis, the generating function has the form:

```
g(n) = ((1 + Z)(2 + Z)(3 + Z) … (n − 1 + Z)) / n
     = Σ P(n, k) · Zᵏ
```

- The **coefficient of Zᵏ** is the probability that action `A` occurs exactly `k` times.
- The **derivative** of the generating function, evaluated at the right point, gives the expected value (mean).
- If a generating function factors into simpler generating functions, the mean of the product is the sum of the means of the factors.

## The punchline

For `n = 1,000,000`, the expected number of times `A` fires is the `n`-th **harmonic number** `H_n ≈ ln n`. So a million-element find-max updates the running max about `ln(10⁶) ≈ 13.8` times on average.

## Key takeaways

- Mathematical analysis adds a quantitative dimension to what we know about a program beyond worst-case big-O.
- Techniques build on each other: decision trees, generating functions, harmonic-number asymptotics all show up repeatedly in algorithm analysis.

## Open threads

- Write a short permanent note: "The average number of running-max updates is `H_n ≈ ln n`." That is a clean, counter-intuitive fact (many expect `n/2`).
- Link this to a future `generating-functions` note and a `harmonic-numbers` note.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/0f7a260c6a534f008d061f0ac83e300f). See [[notion-migration]].*

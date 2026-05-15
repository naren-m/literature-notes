---
title: "Generating Functions"
date: 2020-09-04
type: research
category: "math/combinatorics"
tags: [math, combinatorics, sequences]
status: seedling
source: "https://www.notion.so/fd4e71e171844053a106a4f8b3689e20"
external: "http://www.math.cmu.edu/~lohp/docs/math/2011-228/mit-ocw-generating-func.pdf"
related: ["[[generating-functions-brilliant]]", "[[harmonic-series]]", "[[number-theory-practicals]]"]
---

# Generating Functions

A generating function is a (possibly infinite) polynomial whose coefficients correspond to the terms in a sequence of numbers $a_n$.

## Definition

Given a sequence $a_0, a_1, a_2, \dots$, its ordinary generating function is

$$G(x) = \sum_{n=0}^{\infty} a_n x^n.$$

The coefficients carry the sequence; the variable $x$ is a formal placeholder, not a value to be evaluated.

## Why they work

Generating functions transform problems about sequences into problems about functions. This unlocks tools that are awkward to apply term-by-term:

- [Partial fractions](https://brilliant.org/wiki/partial-fractions/) to split rational generating functions.
- [Polynomial multiplication](https://brilliant.org/wiki/polynomial-multiplication/) to compute convolutions of sequences.
- [Differentiation rules](https://brilliant.org/wiki/differentiation-rules/) to shift indices and pull out factors of $n$.

They are especially effective at solving [recurrence relations](https://brilliant.org/wiki/recurrence-relations/): re-express the recurrence as a functional equation in $G(x)$, solve for $G(x)$, then read off coefficients.

## Sources

- MIT OCW — [mit-ocw-generating-func.pdf](http://www.math.cmu.edu/~lohp/docs/math/2011-228/mit-ocw-generating-func.pdf) (attached to the original Notion page).
- Brilliant Math & Science Wiki — see [[generating-functions-brilliant]].

## Open threads

- Worked example: Fibonacci via `G(x) = x / (1 − x − x²)` → partial fractions → closed form.
- Exponential generating functions and their role in counting labelled structures.
- Connection with the `z`-transform used in DSP.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/fd4e71e171844053a106a4f8b3689e20). See [[notion-migration]].*

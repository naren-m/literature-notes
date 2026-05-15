---
title: "Exponents"
date: 2020-09-09
type: research
category: "math/algebra"
tags: [math, algebra, basics]
status: seedling
source: "https://www.notion.so/62e380df816349ba8ab1010cf261bdfe"
related: ["[[logarithms]]", "[[asymptotic-notations]]", "[[generating-functions]]"]
---

# Exponents

An exponent is the number of times you multiply a number by itself (with a hidden `1` as the starting value — i.e. `x^0 = 1`).

## Definition

`a^n = a × a × … × a`  (`n` times, with `a^0 = 1`)

## Growth-rate framing

`2^5 = 32` reads as:

- **2** — growth rate (the factor by which you multiply each step).
- **5** — time you grow for (the number of steps).
- **32** — result.

This framing makes exponentials the natural language for compounding processes: each unit of "time" multiplies by the growth rate, regardless of the current value.

## Properties

Standard identities (over the reals or positive reals where applicable):

- `a^m · a^n = a^{m+n}`
- `a^m / a^n = a^{m−n}`
- `(a^m)^n = a^{m·n}`
- `(a·b)^n = a^n · b^n`
- `a^{-n} = 1 / a^n`
- `a^{1/n} = nth root of a`

## Relationship to logarithms

The [[logarithms|logarithmic function]] undoes the exponential function: `log_a(a^x) = x` and `a^{log_a(x)} = x`. This duality is why exponentials and logarithms show up as a pair in [[asymptotic-notations|asymptotic analysis]], information theory, and any compounding / decay process.

## Open threads

- Differentiate polynomial growth (`n^c`) from exponential growth (`c^n`) — the latter eventually dominates for any `c > 1`.
- Hook into [[generating-functions]] where powers of `x` carry the sequence index.
- Continuous growth and the role of `e`.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/62e380df816349ba8ab1010cf261bdfe). See [[notion-migration]].*

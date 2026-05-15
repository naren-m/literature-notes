---
title: "Hashing"
date: 2021-01-25
type: research
category: "algorithms/data-structures"
tags: [hashing, data-structures, algorithms]
status: seedling
source: "https://www.notion.so/161c49b4057e480ea3a99bf1ceb960d5"
related: ["[[data-structures-and-algorithms]]", "[[asymptotic-notations]]"]
---

# Hashing

A hash function `h(k)` maps a key `k` into a slot in a hash table of size `m`. Different construction methods trade off distribution quality against implementation complexity.

## Division method

`h(k) = a mod b`

Simple and fast. Choice of `b` (the table size) matters — a prime far from a power of two is usually preferred to avoid pathological collisions.

## Multiplication method

`h(k) = floor(m * (k * A mod 1))`

Pick a constant `A` in `(0, 1)`, multiply, take the fractional part, scale by `m`. Knuth suggests `A ≈ (√5 − 1) / 2`. Less sensitive to the choice of `m` than the division method.

## Universal hashing

`h(k) = ((a·k + b) mod P) mod m`

- `a`, `b` are random numbers less than `P`.
- `P` is a prime larger than the key universe `m`.

### Collision bound

In the worst case for distinct keys `k₁ ≠ k₂`:

`Pr_{a,b} {h(k₁) == h(k₂)} = 1/m`

i.e. the expected number of collisions per bucket (the load factor) is `1/m`. Universal families give provably good behaviour for any adversarial input.

## Open threads

- Relationship to [[counting-sort]] and [[radix-sort]]: all three avoid comparisons by using the key itself as an index.
- When does double hashing or cuckoo hashing pay off over chaining?
- Hash-table resizing / rehashing cost analysis — amortised `O(1)` per insert under doubling.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/161c49b4057e480ea3a99bf1ceb960d5). See [[notion-migration]].*

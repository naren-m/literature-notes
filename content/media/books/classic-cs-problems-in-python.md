---
title: "Classic Computer Science Problems in Python"
date: 2020-08-08
type: literature
category: "cse/programming"
tags: [python, algorithms, recursion, memoization, cs]
status: next-up
source: "https://www.notion.so/f7fe8cb2aba74ae0bc9fe3af1f186fd7"
external: "https://learning.oreilly.com/library/view/classic-computer-science/9781617295980/"
related: ["[[recursion]]", "[[memoization]]", "[[dynamic-programming]]"]
---

# Classic Computer Science Problems in Python

A classical CS problems reader written in Python. Captured here as a chapter-by-chapter roadmap plus early Chapter 1 notes.

> Python is loved for its flexibility, beautiful and succinct syntax, object-oriented purity, and bustling community.
>
> Some say computers are to computer science as telescopes are to astronomy.

## Chapter 1 — Recursion, Memoization, Bit Manipulation

### Fibonacci

If the value at step *n* depends on the previous two, you're in Fibonacci territory: `fib(n) = fib(n-1) + fib(n-2)`.

```python
def fib(n):
    return fib(n-1) + fib(n-2)
```

Missing the base case → infinite recursion. The programmer's duty is to avoid that.

```python
def fib2(n):
    if n < 2:  # base case
        return n
    return fib2(n-1) + fib2(n-2)
```

This *works* for small `n` but blows up at `fib2(25)` — every call spawns two more, so the call stack grows exponentially.

### Memoization

Cache computed values so you never redo them. Donald Michie coined the term *memoization* in 1967 (Edinburgh, Dept of Machine Intelligence).

```python
memo = {0: 0, 1: 1}

def fib3(n):
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]
```

Open threads: auto-memoization via `functools.lru_cache`, and the iterative-loop version.

### Trivial compression

Compression encodes data to take less space; decompression reverses it. Classic example — DNA nucleotides take one of four values (A, C, G, T), so 2 bits per nucleotide suffices:

```
A = 00    C = 01    G = 10    T = 11
```

Conceptually related to the Bloom filter (seen in the Cisco Python 3 course).

## Roadmap — remaining chapters

- **Ch 2** — Search: binary, DFS, BFS, A\*.
- **Ch 3** — Eight queens, map-colouring, cryptarithmetic (SEND + MORE = MONEY).
- **Ch 4** — Building graph data structures; optimisation problems.
- **Ch 5** — Genetic algorithms.
- **Ch 6** — K-means clustering.
- **Ch 7** — Neural networks.
- **Ch 8** — Adversarial search in two-player perfect-information games (chess, checkers, Connect Four).
- **Ch 9** — More fun problems.

## Links

- O'Reilly reader — [learning.oreilly.com/library/view/classic-computer-science](https://learning.oreilly.com/library/view/classic-computer-science/9781617295980/)
- Problems git repo bookmarked inside the original Notion page.

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/f7fe8cb2aba74ae0bc9fe3af1f186fd7). See [[notion-migration]].*

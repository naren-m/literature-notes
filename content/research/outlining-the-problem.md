---
title: "Outlining the Problem — Programming Approach"
date: 2020-05-25
type: research
category: "CSE/software-engineering"
tags: [problem-solving, programming, testing, poker]
status: incomplete
source: "Notion Notes DB, course exercise: 'Write a Poker program'"
related: []
---

# Outlining the Problem — Programming Approach

A lightweight method for attacking a programming problem: inventory the problem, decompose into functions, write a test alongside each function, and probe extreme values. Captured from a course exercise on writing a Poker program.

## The method

1. **Take inventory of the problem.** Write down every rule, constraint, and boundary you can think of before writing code. Don't skip this — most bugs live in the gap between "what I thought the problem was" and "what the problem actually is."
2. **Decompose into functions.** Each piece of the specification becomes one function.
3. **Write a test alongside each function.** Tests are not an afterthought — they are part of the specification.
4. **Probe extreme values.** A core principle of testing is hammering the edges: empty input, single element, max size, negative numbers, duplicate values, etc.

## Worked example: Poker

To write a program that ranks poker hands, the inventory step surfaces the needed concepts:

- **Hand ranks**:
  - *n-of-a-kind* (pair, three-of-a-kind, four-of-a-kind).
  - *Straight* — five cards in sequence (e.g., `5, 6, 7, 8, 9`).
  - *Flush* — all five cards share a suit.
  - *Straight flush* — both conditions together.
- Each hand rank becomes a function (`is_pair`, `is_straight`, `is_flush`, …) paired with a unit test.

## Why this matters

Outlining forces you to *think* before you type. The common failure mode is to start coding against a half-remembered spec and discover edge cases only when tests fail (or, worse, when users hit them). Inventory + test-first decomposition is a forcing function against that failure mode.

## Candidate permanent notes

- **"Take inventory before writing code."** A short mnemonic for the outlining discipline.
- **"Test extremes, not averages."** Most bugs live at the boundary of the input space.

## Open threads

- Try this method on a non-trivial exercise end-to-end and record how much it reduces rework time versus the "just start coding" baseline.
- Compare against formal specifications (e.g., TLA+) and lightweight design docs — where does each pay off?

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/a738876f66a04bfe9f8475772fcd7bb4). See [[notion-migration]].*

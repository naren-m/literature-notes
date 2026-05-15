---
title: "Clean Code - Lesson 1 (Uncle Bob)"
date: 2020-08-25
type: literature
category: "CSE/clean-code"
tags: [clean-code, software-craftsmanship, video, uncle-bob]
status: incomplete
source: "https://www.youtube.com/watch?v=7EmboKQH8lM"
related: []
---

# Clean Code — Lesson 1

Video notes from Robert C. Martin's Clean Code lecture series, lesson 1. Timestamps preserved for reference back to the source.

- Agile Manifesto
- Software Craftsmanship Manifesto

## Opening aside — How far is the sun?

- ~150 million km
- 8 light-minutes
- Referenced in video: [Aristarchus of Samos](https://en.wikipedia.org/wiki/Aristarchus_of_Samos) estimating lunar distance.

## Table of contents (with timestamps)

- [4:49](https://www.youtube.com/watch?v=7EmboKQH8lM&t=289s) — How far is the sun?
- [10:52](https://www.youtube.com/watch?v=7EmboKQH8lM&t=652s) — Introduction to Clean Code
- [12:21](https://www.youtube.com/watch?v=7EmboKQH8lM&t=741s) — The current society works with software
- [19:47](https://www.youtube.com/watch?v=7EmboKQH8lM&t=1187s) — Volkswagen case / ethics of software development
- [24:28](https://www.youtube.com/watch?v=7EmboKQH8lM&t=1468s) — Why are programmers so slow?
- [32:13](https://www.youtube.com/watch?v=7EmboKQH8lM&t=1933s) — What is clean code?
- [40:09](https://www.youtube.com/watch?v=7EmboKQH8lM&t=2409s) — Analyzing some lines of code
- [43:43](https://www.youtube.com/watch?v=7EmboKQH8lM&t=2623s) — Long code is not good code
- [49:25](https://www.youtube.com/watch?v=7EmboKQH8lM&t=2965s) — Good code / refactored function
- [52:40](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3160s) — Polite code / rules for writing a newspaper article
- [55:25](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3325s) — Shrunk code / rules of functions
- [1:00:23](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3623s) — Shrunk code / drawing a function
- [1:05:36](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3936s) — When and why was Java invented?
- [1:08:52](https://www.youtube.com/watch?v=7EmboKQH8lM&t=4132s) — Prose code / arguments
- [1:16:13](https://www.youtube.com/watch?v=7EmboKQH8lM&t=4573s) — Avoid switch statements / problems and evolution of some languages
- [1:27:22](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5242s) — Output arguments, no side effects / garbage collection
- [1:32:21](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5541s) — No side effects / using lambda
- [1:34:26](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5666s) — Command and query separation
- [1:35:30](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5730s) — Prefer exceptions to returning error codes
- [1:37:05](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5825s) — DRY principle
- [1:39:21](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5961s) — Structured programming / Dijkstra vs actual practice
- [1:45:32](https://www.youtube.com/watch?v=7EmboKQH8lM&t=6332s) — Science and correct software

## Key points captured

### Polite code ([52:40](https://www.youtube.com/watch?v=7EmboKQH8lM&t=3160s))

- Polite code does not jump between abstractions.
- Fundamental rule for a function: every line of a function should be at the same level of abstraction, and the level should be one below the function's name.

### No side effects — using lambda ([1:32:21](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5541s))

- Open/Closed Principle: a module should be open for extension but closed for modification. Use base classes and derivatives.

### Command / Query Separation ([1:34:26](https://www.youtube.com/watch?v=7EmboKQH8lM&t=5666s))

- Commands change state and return void.
- Queries return values and do not change state.
- Convention: a function that returns a value should not have a side effect. This discipline makes side effects tractable.

## Rules of thumb

- Principle of least surprise.
- Avoid passing booleans to functions (mostly).
- Avoid switch statements. See [video segment](https://youtu.be/7EmboKQH8lM?t=4617). (Why? — not yet captured.)

---

*Migrated from Notion on 2026-04-19. Original: [Notion page](https://www.notion.so/4920af3d4dea4886b89a4aaaacea45c4). See [[notion-migration]].*

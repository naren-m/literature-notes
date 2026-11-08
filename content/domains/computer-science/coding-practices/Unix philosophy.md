---
title: "Unix philosophy"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Coding Practices"
tags: ["software-design", "unix", "tools"]
status: "draft"
source: "https://en.wikipedia.org/wiki/Unix_philosophy"
related: ["[[Maintaining code base]]", "[[Persistent LLM wikis make synthesis compounding]]", "[[Decorator Pattern]]", "[[Brian Kernighan]]", "[[Brian Kernighan interview]]", "[[Hello World]]"]
---

# Unix philosophy

Small tools. Each does one job well. They talk through simple interfaces. Easy to test, easy to replace.

Started with Ken Thompson. Doug McIlroy wrote it down in the Bell System Technical Journal (1978). Peter H. Salus boiled it to three lines in *A Quarter-Century of Unix* (1994):

- Write programs that do one thing and do it well.
- Write programs to work together.
- Write programs to handle text streams, because that is a universal interface.

McIlroy's version has more teeth. Build afresh rather than pile "features" onto old programs. Expect your output to become the input of some program you don't know yet, so don't clutter it. Try things early, within weeks, and throw away the clumsy parts. Build tools, even if you have to detour to build them and throw some out later.

## Why it works

Here is the thing. Software gets powerful when its parts can be combined in ways the original author never thought of. Text streams, predictable behavior, narrow responsibilities. That's what makes the combining possible.

## It's also a maintenance philosophy

A small tool you can understand, test, rewrite, or throw away without dragging the whole system along. That's why I connect it to [[Maintaining code base]]. Same goes for plain-text knowledge systems, where notes, scripts and indexes can each get better on their own.

https://en.wikipedia.org/wiki/Unix_philosophy

- [[Maintaining code base]]
- [[Persistent LLM wikis make synthesis compounding]]
- [[Decorator Pattern]]

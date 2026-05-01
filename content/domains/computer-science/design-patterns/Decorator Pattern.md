---
title: "Decorator Pattern"
date: 2026-04-30
type: permanent
category: "Computer Science/Design Patterns"
tags: [design-patterns, software-design]
status: draft
related: ["[[Design Patterns]]", "[[Unix philosophy]]", "[[Leaky abstraction]]"]
---

# Decorator Pattern

The decorator pattern adds behavior by wrapping an object instead of changing the object's class or editing the original implementation.

The wrapper exposes the same interface as the wrapped object, delegates the base behavior, and adds work before or after delegation. This keeps extension separate from the core object and lets multiple behaviors be composed in layers.

The tradeoff is indirection. Decorators can keep a design open to extension, but too many wrappers can hide where behavior actually comes from and create a [[Leaky abstraction]].

## Related

- [[Design Patterns]]
- [[Unix philosophy]]
- [[Leaky abstraction]]

---
title: "Decorator Pattern"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Design Patterns"
tags: ["design-patterns", "software-design"]
status: "draft"
related: ["[[Design Patterns]]", "[[Unix philosophy]]", "[[Leaky abstraction]]"]
---

# Decorator Pattern

- Wrap, don't edit.
- Same interface as the wrapped object. Delegate, then add work before or after.
- Behaviors stack in layers. Core object stays untouched.
- Cost = indirection. Too many wrappers and you can't tell where behavior comes from → [[Leaky abstraction]].

## Related
- [[Design Patterns]]
- [[Unix philosophy]]
- [[Leaky abstraction]]

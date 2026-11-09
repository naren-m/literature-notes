---
title: "Leaky abstraction"
date: "2026-05-05"
type: "research"
category: "Legacy/Pages"
tags: ["programming", "design"]
status: "draft"
---

# Leaky abstraction

- A design flaw where an abstraction, meant to simplify and hide the underlying complexity of the system, fails to completely do so.
- Some implementation details get exposed, `leaking` through the abstraction, forcing users to know the underlying complexity to use it well.
- Concept popularized by Joel Spolsky, who coined the term.
- Law of leaky Abstractions
  - All non-trivial abstractions, to some degree, are leaky.

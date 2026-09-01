---
title: "Testing Principles"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Coding Practices"
tags: ["testing", "quality", "maintainability"]
status: "complete"
related: ["[[Testing Pyramid]]", "[[Test Driven Dev]]"]
---

# Testing Principles

Code should be written so that its important behavior can be tested.

That means keeping responsibilities clear, choosing readable behavior over clever behavior, and exposing enough observable state to verify results. A test should check behavior that matters to users or operators, not only increase a coverage number.

Use the cheapest test that proves the behavior: unit tests for isolated rules, integration tests for component boundaries, and end-to-end tests for real workflows. Every change should include or update an automated check when one is practical.

Testing is part of maintainability. It makes regressions visible, shortens diagnosis, and makes future changes safer. [[Testing Pyramid]] describes the cost and scope trade-off between test levels.

## Related

- [[Testing Pyramid]]
- [[Test Driven Dev]]
- [[State Coverage]]

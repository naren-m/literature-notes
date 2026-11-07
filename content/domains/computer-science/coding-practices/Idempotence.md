---
title: "Idempotence"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Coding Practices"
tags: ["programming", "reliability", "distributed-systems"]
status: "draft"
source: "https://en.wikipedia.org/wiki/Idempotence"
related: ["[[Test Driven Dev]]", "[[Testing Principles]]", "[[DesigningDistributedSystems]]"]
---

# Idempotence

Run it once or run it ten times → same result.

- Retries are unavoidable. Networks fail, jobs restart, users click submit twice.
- Idempotent op = safe to retry. No double charges, no duplicate records.
- Reliability property, not a math curiosity.
- Easier to test, easier to reason about, easier to recover after partial failure.

- [[Test Driven Dev]]
- [[Testing Principles]]
- [[DesigningDistributedSystems]]

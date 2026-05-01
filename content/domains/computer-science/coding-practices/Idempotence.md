---
title: "Idempotence"
date: 2026-04-30
type: permanent
category: "Computer Science/Coding Practices"
tags: [programming, reliability, distributed-systems]
status: draft
source: "https://en.wikipedia.org/wiki/Idempotence"
related: ["[[Test Driven Dev]]", "[[Testing Principles]]", "[[DesigningDistributedSystems]]"]
---

# Idempotence

An operation is idempotent when running it more than once has the same durable effect as running it once.

This matters in software because retries are unavoidable. Networks fail, jobs restart, and users resubmit requests. If an operation is idempotent, the system can safely repeat it without creating duplicate side effects such as double charges, duplicate records, or inconsistent state.

Idempotence is therefore a reliability property, not just a mathematical curiosity. It makes systems easier to test, reason about, and recover after partial failure.

## Related

- [[Test Driven Dev]]
- [[Testing Principles]]
- [[DesigningDistributedSystems]]

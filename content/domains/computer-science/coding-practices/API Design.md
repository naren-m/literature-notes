---
title: "API Design"
date: 2026-11-11
type: permanent
category: "Computer Science/Coding Practices"
tags: ["api", "design"]
status: draft
related: ["[[Python Decorators]]", "[[Idempotence]]", "[[Unix philosophy]]"]
---
# API Design

The interface other code calls. Once callers depend on it, changing it breaks them.

- Small surface. Consistent names. Hard to misuse.
- Errors explicit, not hidden.
- Retries safe → [[Idempotence]]
- Add behavior without changing the signature → [[Python Decorators]]
- Do one thing well → [[Unix philosophy]]

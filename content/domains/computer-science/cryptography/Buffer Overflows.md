---
title: "Buffer Overflows"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "memory-safety", "vulnerabilities"]
status: "draft"
related: ["[[Security Vulnerabilities]]", "[[Zero Day Attack]]", "[[Side Channel Attack]]"]
---

# Buffer Overflows

Write more data than the buffer can hold → the extra bytes spill into nearby memory.

- Overwrite the neighbours → corrupt state, crash the process, bypass checks, or redirect execution.
- Classic class of [[Security Vulnerabilities]]. Unknown to defenders → [[Zero Day Attack]].
- Fix = boundary discipline. ALWAYS check the size before copying, parsing or receiving untrusted input.

- [[Side Channel Attack]]

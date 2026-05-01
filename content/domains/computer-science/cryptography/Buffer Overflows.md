---
title: "Buffer Overflows"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, memory-safety, vulnerabilities]
status: draft
related: ["[[Security Vulnerabilities]]", "[[Zero Day Attack]]", "[[Side Channel Attack]]"]
---

# Buffer Overflows

A buffer overflow happens when a program writes more data into a fixed-size memory region than that region can hold.

The security risk is that the extra data can overwrite nearby memory. In unsafe languages or poorly bounded code paths, that overwrite can corrupt state, crash the process, bypass checks, or redirect execution. This makes buffer overflows a common class of [[Security Vulnerabilities]] and a possible form of [[Zero Day Attack]] when the flaw is unknown to defenders.

The durable lesson is boundary discipline: code that copies, parses, or receives untrusted input must enforce explicit size limits before writing into memory.

## Related

- [[Security Vulnerabilities]]
- [[Zero Day Attack]]
- [[Side Channel Attack]]

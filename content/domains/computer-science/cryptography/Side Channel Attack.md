---
title: "Side Channel Attack"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, cryptography, hardware]
status: draft
related: ["[[Cryptography]]", "[[Cache prefetching]]", "[[Rowhammer]]"]
---

# Side Channel Attack

A side channel attack extracts secrets from indirect signals instead of from the intended input or output of a system.

Examples include timing differences, power use, electromagnetic radiation, sound, cache behavior, and memory disturbance. The attacker is not necessarily breaking the mathematical primitive; they are measuring the implementation or environment around it.

This is why [[Cryptography]] must be implemented with attention to physical and operational behavior. A theoretically secure algorithm can still leak useful information through cache timing, branching, hardware effects, or repeated observable patterns.

## Related

- [[Cryptography]]
- [[Cache prefetching]]
- [[Rowhammer]]

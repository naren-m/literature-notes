---
title: "Rowhammer"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Security"
tags: ["security", "hardware", "memory"]
status: "draft"
related: ["[[Side Channel Attack]]", "[[ECC memory]]", "[[Tampering]]", "[[Cache prefetching]]", "[[Cryptography]]"]
---

# Rowhammer

Hammer one DRAM row again and again → charge leaks → bits flip in neighbouring rows.

- Cause: high cell density in modern DRAM. Isolation between memory cells breaks.
- Example of a [[Side Channel Attack]].
- Combine bit flips → [[Tampering]], privilege escalation, malicious code. Network-based attacks theoretically possible.
- Software assumes hardware enforces isolation. Rowhammer breaks that assumption.

"Necessity is the mother of invention." – Plato
Adversaries keep finding creative ways in. Rowhammer is a perfect example.

[[ECC memory]] was supposed to fix it: detects bit tampering and corrects it. Attack replicated on ECC anyway. Surprise!

Rowhammer on ECC:
1. Templating to locate vulnerable bits. ECC doesn't detect tampering of three consecutive bits.
2. Access time differs for unaltered vs tampered bits. In poker, a tell. Now you know where to hammer.
3. Slow. But templating is virtually undetectable. Map for days, weeks, then launch.

ECC is used in sensitive systems (financial, IoT), so this hurts.
Hardware behaviour is part of the threat model.

More: https://bit.ly/2U4EYTg

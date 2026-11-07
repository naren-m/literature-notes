---
title: "Integrity"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: []
status: "draft"
related: ["[[CIA Triad]]", "[[STRIDE]]", "[[Tampering]]", "[[Hashing]]", "[[Message Authentication Code]]", "[[Digital signatures]]"]
---

# Integrity

Data is what it says it is. Unchanged, trustworthy.

- The I in [[CIA Triad]]. Can the system detect unauthorized change?
- [[STRIDE]] → [[Tampering]] is the attack on it.
- How do we check?
  - [[Hashing]] → did the fingerprint change?
  - [[Message Authentication Code]] → hash + shared key
  - [[Digital signatures]] → integrity + who sent it

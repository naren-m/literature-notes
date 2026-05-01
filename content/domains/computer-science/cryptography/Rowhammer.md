---
title: "Rowhammer"
date: 2026-04-30
type: permanent
category: "Computer Science/Security"
tags: [security, hardware, memory]
status: draft
related: ["[[Side Channel Attack]]", "[[ECC memory]]", "[[Tampering]]"]
---

# Rowhammer

Rowhammer is a hardware attack where repeatedly accessing one row of DRAM can disturb nearby rows and flip bits.

The attack matters because it crosses an isolation boundary that software usually assumes is enforced by hardware. If an attacker can induce chosen bit flips, the result can become [[Tampering]], privilege escalation, or corruption of security-critical state.

[[ECC memory]] can reduce some memory corruption risk, but it is not a complete answer. The defensive lesson is that hardware behavior is part of the threat model: density, timing, refresh behavior, and error correction can all affect security.

## Related

- [[Side Channel Attack]]
- [[ECC memory]]
- [[Tampering]]

---
title: "Harvest now decrypt later makes key exchange urgent"
date: 2026-04-30
type: permanent
category: "Computer Science/Cryptography"
tags: [cryptography, post-quantum-cryptography, key-exchange]
status: draft
source: "[[How Quantum Computers Break Encryption: First Principles]]"
related: ["[[Key exchange]]", "[[Confidentiality]]", "[[Data Sensitivity]]", "[[Lattice-based encryption]]"]
---

# Harvest now decrypt later makes key exchange urgent

Harvest-now-decrypt-later attacks make post-quantum [[Key exchange]] urgent even before large quantum computers exist.

An attacker can record encrypted traffic today and wait. If the session's key agreement later becomes breakable, the attacker may recover the old session key and decrypt stored traffic. The exposure depends on the lifetime of the protected data, not just the date when quantum computers become practical.

This changes migration priority. Data with long-lived [[Confidentiality]] requirements needs quantum-resistant key agreement before the cryptographic break arrives. Short-lived data may tolerate a slower migration path, but medical, legal, financial, government, or trade-secret material cannot assume that "safe today" means "safe for its whole useful life."

## Related

- [[Key exchange]]
- [[Confidentiality]]
- [[Data Sensitivity]]
- [[Lattice-based encryption]]

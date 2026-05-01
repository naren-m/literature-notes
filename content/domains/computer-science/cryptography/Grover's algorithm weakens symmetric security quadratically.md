---
title: "Grover's algorithm weakens symmetric security quadratically"
date: 2026-04-30
type: permanent
category: "Computer Science/Cryptography"
tags: [cryptography, quantum-computing, encryption]
status: draft
source: "[[How Quantum Computers Break Encryption: First Principles]]"
related: ["[[Encryption]]", "[[Block Cipher]]", "[[ENTROPY]]", "[[Quantum attacks depend on exploitable mathematical structure]]"]
---

# Grover's algorithm weakens symmetric security quadratically

Grover's algorithm gives quantum computers a square-root speedup for brute-force search, not a complete break of symmetric encryption.

For an n-bit key, exhaustive search classically costs about 2^n trials. Grover's algorithm lowers that to about 2^(n/2) quantum search steps. That is a real reduction, but it is very different from the structural break Shor's algorithm gives against RSA and ECC.

The practical result is that key sizes matter. AES-128 has a quantum brute-force work factor roughly comparable to 64-bit classical security, while AES-256 restores the margin to roughly 128-bit quantum search. This is why strong symmetric [[Encryption]] can remain viable in a post-quantum world when configured with sufficient key length.

## Related

- [[Encryption]]
- [[Block Cipher]]
- [[ENTROPY]]
- [[Quantum attacks depend on exploitable mathematical structure]]

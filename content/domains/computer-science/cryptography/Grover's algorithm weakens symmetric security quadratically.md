---
title: "Grover's algorithm weakens symmetric security quadratically"
date: "2026-04-30"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "quantum-computing", "encryption"]
status: "draft"
source: "[[How Quantum Computers Break Encryption: First Principles]]"
related: ["[[Encryption]]", "[[Block Cipher]]", "[[ENTROPY]]", "[[Quantum attacks depend on exploitable mathematical structure]]"]
---

# Grover's algorithm weakens symmetric security quadratically

Grover gives a quantum computer a square-root speedup on brute-force search. That's it. It does not break symmetric encryption.

Simple math. n-bit key. Classical brute force is about 2^n tries. Grover brings it down to about 2^(n/2) quantum search steps. A real reduction. But nothing like what Shor does to RSA and ECC. Shor exploits structure and breaks them outright. Grover just searches faster. (More on that in [[Quantum attacks depend on exploitable mathematical structure]].)

So what do we do? Use bigger keys. AES-128 under Grover is roughly 64-bit classical security. AES-256 brings the margin back to roughly 128-bit quantum search.

That's why strong symmetric [[Encryption]] survives the post-quantum world. Just pick enough key length.

- [[Block Cipher]]
- [[ENTROPY]]

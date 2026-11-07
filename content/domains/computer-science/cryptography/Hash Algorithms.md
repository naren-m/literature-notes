---
title: "Hash Algorithms"
date: "2026-05-05"
type: "permanent"
category: "Computer Science/Cryptography"
tags: ["cryptography", "hashing", "integrity"]
status: "complete"
related: ["[[Hashing]]", "[[Checksum]]", "[[Block Cipher]]"]
---

# Hash Algorithms

Variable length data → fixed length digest. Change one bit → radically different digest.

Secure hash algorithm:
- One-way → must use brute force to reverse. (as in [[Hashing]])
- Collision resistant → unlikely, if not impossible, to find two inputs with the same hash.
- Performant + memory efficient → slow hashes are hard to scale.

Plain hash checks [[Integrity]]. It does not say who produced the data.

Approaches to creating hashes: [[Block Cipher|block cipher]], stream cipher, keyed hash.

Algorithms:
- SHA-256 → most common today. SHA-2 family, 256-bit digest. Good balance between compute and security.
- SHA-384, SHA-512 → also SHA-2. More secure, more compute.
- SHA-3 → available, not widely used.

Only accidental corruption to worry about? A [[Checksum]] is enough.

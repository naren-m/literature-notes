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

A hash algorithm maps input data of any length to a fixed-length digest.

A cryptographic hash should make it difficult to recover the input from the digest, difficult to find two inputs with the same digest, and sensitive to even a small input change. These properties make hashes useful for checking [[Integrity]], but a plain hash does not authenticate who produced the data.

SHA-256 and SHA-512 are members of the SHA-2 family. SHA-3 is another modern hash family. The correct choice depends on the protocol and its security requirements; a checksum is sufficient only when the threat is accidental corruption.
